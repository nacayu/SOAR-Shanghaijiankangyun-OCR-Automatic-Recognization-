# This is a public repo for helping reduce work pressure

## Functions and Performence
- Functions:
1. We utilize the paddleocr lib to automaticlly recognize the picture and transform these pictures into excel which shows the individuals and their corresponding infomation(e.g. test_time, result)
2. You can change our code for your destination.
- Performence:
After testing, it can achieve 30 frames per second.

## Result show

<img src="https://github.com/nacayu/Shanghaijiankangyun_OCR_Automatic_Recognization/blob/main/result.jpg#pic_center" width="300" height="350"></img>


## our enviroment:

1. paddlepaddle:paddlepaddle 2.2.2 cpu version
2. paddleocr 2.4.0.4

## Installation
We install the enviroment(paddlepaddle and paddleocr) by following page:
https://github.com/PaddlePaddle/PaddleOCR

## Use

````# 

#(we have already set up default path)
$cd path/to/Shanghaijiankangyun_OCR_Automatic_Recognization
$python ./main.py --output_path your path --input_path your path


````
