from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap, QImage
from ui import Ui_MainWindow
from pathlib import Path
import sys
import pandas as pd
import cv2
import pytesseract
from PIL import Image
import os
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

class myapp(Ui_MainWindow):
    def __init__(self) -> None:
        self.thai_alphabet = "กขคฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮะอาอิอีอึอือุอูเอะเอแอะแอโอะโอเอาะใอไอเอา"
        self.eng_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        super().setupUi(MainWindow)
        self.file = None
        self.setupSignal()
        self.confirm_bt.clicked.connect(self.get)
        self.ocr_bt.clicked.connect(self.ocr)
        self.dropdown.setCurrentIndex(0)  # Set default language to THA

    def get(self):
        self.inputtext = self.textselected.text()
        print('Text input = ', self.inputtext)

    def setupSignal(self):
        self.input_bt.clicked.connect(self.selectInput)
        self.dropdown.currentIndexChanged['QString'].connect(self.ocr)  # Update your OCR function
        
    def selectInput(self):
        try:
            # Pop up for selecting files
            self.file = QFileDialog.getOpenFileName(caption="Choose image", filter="Image files (*.jpg *.png *.jpeg *.pdf)", directory='/home/cepheusn22/home/')
            try:
                if self.file[0][-4:] == ".pdf":
                    # Convert PDF to images
                    images = convert_from_path(self.file[0])

                    # Save each image as JPEG
                    for i, image in enumerate(images):
                        image_path = os.path.splitext(self.file[0])[0] + f"_{i}.jpg"
                        image.save(image_path, "JPEG")
                        # Process the image or perform OCR on the saved image
                        self.frame = cv2.imread(image_path)
                        self.resized_frame = cv2.resize(self.frame, (800, 590))
                        self.display_image(self.resized_frame)
                        self.file = [image_path]
                else:
                    self.frame = cv2.imread(self.file[0])  # index 0 is directory
                    self.resized_frame = cv2.resize(self.frame, (800, 590))
                    self.display_image(self.resized_frame)
            except:
                pass
        except:
            print("Invalid file")

    def ocr(self):
        try :
            self.ocrbox(self.frame)
        except :
            self.result.setText("No file selected")

    def ocrbox(self, image):
        try :
                
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
            
            #data = pytesseract.image_to_data(thresh, output_type=pytesseract.Output.DICT , lang=self.dropdown.currentText())
            data = pytesseract.image_to_data(thresh, output_type=pytesseract.Output.DICT , lang=self.dropdown.currentText())
            # Remove empty strings from the list
            n_box = len(data['text'])
            text = ""
            for i in range(n_box):
                if int(float(data['conf'][i])) > 80:
                    if len(data['text'][i]) == 1:
                        if data['text'][i] in self.thai_alphabet:
                            text += data['text'][i]
                        elif all(char in self.eng_alphabet for char in data['text'][i]):
                            text += data['text'][i] + " "
                        elif data['text'][i] == ' ':
                            pass
                    elif len(data['text'][i]) > 1:
                        if all(char in self.eng_alphabet for char in data['text'][i]):
                            text += data['text'][i] + " "
                        elif all(char in self.thai_alphabet for char in data['text'][i]) and all(char in self.eng_alphabet for char in data['text'][i+1]):
                            text += data['text'][i] + " "
                        else:
                            text += data['text'][i]
                    try:
                        if data['text'][i] == self.inputtext:
                            (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
                            cv2.rectangle(self.resized_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    except:
                        pass

            self.display_image(self.resized_frame)
            print(text)
            self.result.setText(text)
        except :
            self.result.setText("No file selected")

    def display_image(self, image):
        h, w, c = image.shape
        step = c * w
        qImg = QImage(image.data, w, h, step, QImage.Format_RGB888)
        self.images.setPixmap(QPixmap.fromImage(qImg))

obj = myapp()

if __name__ == "__main__":
    MainWindow.show()
    sys.exit(app.exec_())
