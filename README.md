# SimpleOCR
In this Project a simple OCR application is written by python. The sample image and result is avalaible as below.
```bash
pip install pytesseract 
pip install cv2
```
![alt text](https://github.com/AIAML/SimpleOCR/raw/master/test.png)

## how pytesseract
1. Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki

2. Note the tesseract path from the installation. Default installation path at the time of this edit was: C:\Users\USER\AppData\Local\Tesseract-OCR. It may change so please check the installation path.

3. pip install pytesseract

4. Set the tesseract path in the script before calling image_to_string:

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
