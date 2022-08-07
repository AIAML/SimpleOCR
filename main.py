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
    filename = "C:\\test3.jpg"
    #img1 = np.array(Image.open(filename))
    #img = cv2.imread(r'C:\\test.png')
    #image = cv2.imread('C:\\test3.jpg', 0)
    #thresh = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)[1]

    #blur = cv2.GaussianBlur(thresh, (3, 3), 0)
    #result = 255 - blur

    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'

    #text = pytesseract.image_to_string(result, lang='fas')
    #print_hi(text)
    img = cv2.imread('C:\\test3.jpg')

    text = pytesseract.image_to_string(img, lang='fas')
    print_hi(text)


    img2 = cv2.imread('C:\\test3.jpg')
    d = pytesseract.image_to_data(img2, lang='fas', output_type=Output.DICT)
    keys = list(d.keys())

    #date_pattern = '[\u0622\u0627\u0628\u067E\u062A-\u062C\u0686\u062D-\u0632\u0698\u0633-\u063A\u0641\u0642\u06A9\u06AF\u0644-\u0648\u06CC]'
    persian_numbers = u'۱۲۳۴۵۶۷۸۹۰'
    persian_regexp = u"(%s)" % u"|".join(persian_numbers)
    date_pattern = persian_regexp

    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(float(d['conf'][i])) > 60:
            if re.match(date_pattern, d['text'][i]):
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('img', img)
    cv2.imwrite('c:\\test4.jpg', img)
    cv2.waitKey(0)
"""
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    print(d.keys())

    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(float(d['conf'][i])) > 20:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('img', img)
    cv2.imwrite('c:\\test4.jpg',img)
    cv2.waitKey(0)
"""
#as
