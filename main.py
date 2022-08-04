from PIL import Image
import pytesseract
import numpy as np
import cv2
from pytesseract import Output

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
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    text = pytesseract.image_to_string(img, lang='fas')
    print_hi(text)
    print(d.keys())

    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(float(d['conf'][i])) > 20:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('img', img)
    cv2.imwrite('c:\\test4.jpg',img)
    cv2.waitKey(0)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
