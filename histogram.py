from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import cv2
import random

class Histogram(FigureCanvas):
 
    def __init__(self, imsource, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Minimum,
                QSizePolicy.Minimum)
        FigureCanvas.updateGeometry(self)
        
        self.img = cv2.imread(imsource)
        
        self.data_r = np.zeros(256)
        self.data_g = np.zeros(256)
        self.data_b = np.zeros(256)
        
        self.plot()
        

    def plot(self):
        arr = [i for i in range(256)]
        

        shape = self.img.shape

        for i in range(shape[0]):
            for j in range(shape[1]):
                self.data_r[self.img[i,j,2]] += 1
                self.data_g[self.img[i,j,1]] += 1
                self.data_b[self.img[i,j,0]] += 1
        
        ax = self.figure.add_subplot(311)
        ax.bar(arr, self.data_r, width = 0.6, color='red')

        ax = self.figure.add_subplot(312)
        ax.bar(arr, self.data_g, width = 0.6, color='green')
        
        ax = self.figure.add_subplot(313)
        ax.bar(arr, self.data_b, width = 0.6, color='blue')
        
        self.draw()
