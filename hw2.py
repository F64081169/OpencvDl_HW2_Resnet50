from PyQt5 import QtCore, QtGui, QtWidgets
import Camera_Calibration
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QTextEdit
from hw2_ui import Ui_MainWindow
import os
import sys
import glob
import scipy
import argparse
import cv2 as cv
import numpy as np
import PIL.Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PyQt5.QtWidgets import QMainWindow, QApplication,QTextEdit
from scipy import signal
from scipy import misc
import imutils
 
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.onBindingUI()

    def onBindingUI(self):    
        self.pushButton.clicked.connect(self.Find_corner)
        self.pushButton_2.clicked.connect(self.Find_Intrinsic)
        self.pushButton_3.clicked.connect(self.Find_Extrinsic)
        self.pushButton_4.clicked.connect(self.Find_distortion)
        self.pushButton_5.clicked.connect(self.Show_result)

    def Find_corner(self) :
        Camera_Calibration.find_corners()
    def Find_Intrinsic(self) :
        Camera_Calibration.find_intrinsic()
    def Find_Extrinsic(self) :
        number = self.textEdit.toPlainText()
        Camera_Calibration.find_extrinsic(int(number))
    def Find_distortion(self) :
        Camera_Calibration.find_distortion()
    def Show_result(self) :
        Camera_Calibration.show_result()


if __name__ == '__main__':  
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())