import sys
import pylab
import matplotlib.pyplot as plt
import cv2 as cv
import keras.backend as K
import pandas as pd
import numpy as np
import glob
import os
from PyQt5.QtWidgets import QMainWindow, QApplication
from matplotlib import pyplot as plt
from keras.datasets import cifar10
from keras.models import load_model ,model_from_json
from tensorflow.keras.utils import to_categorical
from hw2Q5_ui import Ui_MainWindow
from keras.preprocessing.image import ImageDataGenerator,load_img ,img_to_array
from sklearn.model_selection import train_test_split
from keras.models import load_model

cont4 = 0
coin01num = 0
coin02num = 0
machingKpoint1 = 0
machingKpoint2 = 0
img4_match = 0
list_keypoints1 = []
list_keypoints2 = []
model = load_model('./original/resnet50_best.h5')

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.onBindingUI()

    def onBindingUI(self):
        self.btn5_1.clicked.connect(self.on_btn5_1_click)
        self.btn5_2.clicked.connect(self.on_btn5_2_click)
        self.btn5_3.clicked.connect(self.on_btn5_3_click)
        self.btn5_4.clicked.connect(self.on_btn5_4_click)
    
    def on_btn5_1_click(self):
        
        model.summary()

    def on_btn5_2_click(self):
        acc = cv.imread("./original/messageImage_1640165525139.jpg", cv.IMREAD_COLOR)
        cv.imshow('TensorBoard',acc)
        
    def on_btn5_3_click(self):
        i = int(self.textEdit.toPlainText())
        filename = "./new_test/"+str(i)+".jpg"
        img = load_img(filename, target_size=(224, 224))
        # convert to array
        img = img_to_array(img)
        # reshape into a single sample with 3 channels
        img = img.reshape(1, 224, 224, 3)
        # center pixel data
        img = img.astype('float32')
        img = img - [123.68, 116.779, 103.939]
        result = model.predict(img)
        print(result)
        #result = result.sum()/2
        if(result[0][0] < result[0][1]):
            label = "Dog"
        else:
            label = "Cat"  
        image = plt.imread(filename)
        plt.title("Class: "+label)
        plt.imshow(image)
        pylab.show()    

    def on_btn5_4_click(self):
        img = cv.imread('noRE_vs_withRE.png')
        cv.imshow('Random-Erasing effect comparison', img)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
