from PIL import Image
import pytesseract
import numpy as np
import cv2


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.

    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filename = "C:\\test-image.png"
    img1 = np.array(Image.open(filename))
    #img = cv2.imread(r'C:\\test.png')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(img1)
    print_hi(text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
