from paddleocr import PaddleOCR, draw_ocr, PPStructure, draw_structure_result, save_structure_res
import os
import argparse
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
from PIL import Image
import pandas as pd
import numpy as np
import re

need_search = ('姓名','证件号码','在沪地址','联系方式','采样时间','检测结果')

def file_process(file_path):
    name_list = []
    for _, _, filenames in os.walk(file_path):
        for img_name in filenames:
            img_name = img_name.split('.')[0]
            img_name = img_name.split('_')[0]
            name_list.append(img_name)
    return name_list
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_path', type=str, default='./image')
    parser.add_argument('--out_path', type=str, default='./output')
    parser.add_argument('--image_name', type=str, default='')
    parser.add_argument('--data', type=str, default='')
    args = parser.parse_args()
    ocr = PaddleOCR(use_angle_cls = False, lang = "ch")
    results = []

    if not args.image_name == '':
        img_path = os.path.join(args.image_path, args.image_name)
        result = ocr.ocr(img_path, cls=True)
        print(result)
    else:
        name_list= file_process(args.image_path)
        print(name_list, len(name_list))
        for parent, dirnames, filenames in os.walk(args.image_path):
            for img in filenames:
                img_path = os.path.join(args.image_path, img)
                res = ocr.ocr(img_path, cls=True)
                results.append(res)
        # print(len(results))
        # print(results[0])
        total_result = []
        for idx, res in enumerate(results):
            name_info = []
            for data in res:
                x, y = data[0][0][0], data[0][0][1]
                info = data[1][0]
                final = (x, y, info)
                name_info.append(final)
            print(name_info)
            person_result = [None, None, None]
            j = 0
            for i, x in enumerate(name_info):
                if x[2] == '姓名':
                    person_result[0] = name_info[i+1][2]
                    j+=1
                elif x[2] == '采样时间':
                    person_result[1] = name_info[i+1][2]
                    mat = re.search(r'\d{4}-\d{1,2}-\d{2}', person_result[1])
                    person_result[1] = mat.group()
                    j+=1
                elif x[2] == '检测结果':
                    person_result[2] = name_info[i+1][2][:7]
                    j+=1
                if j == 3:
                    print(person_result)
                    break
            total_result.append(person_result)
        print(total_result)
    total_result = np.array(total_result)
    df = pd.DataFrame({
        '姓名':total_result[:, 0],
        '采样时间':total_result[:, 1],
        '检测结果':total_result[:, 2]
    })
    print(df)
    if not os.path.exists(args.out_path):
        os.mkdir(args.out_path)
    df.to_excel(os.path.join(args.out_path, 'output.xlsx'))






if __name__ == "__main__":
    main()