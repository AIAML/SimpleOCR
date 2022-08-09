from PIL import Image
import pytesseract
import numpy as np
import cv2
from pytesseract import Output
import re
from unidecode import unidecode

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.

    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
    img = cv2.imread(r'C:\\test.png')
    text = pytesseract.image_to_string(img)
    print_hi(text)

    cv2.imshow('img', img)
    cv2.imwrite('c:\\test4.jpg',img)
    cv2.waitKey(0)
