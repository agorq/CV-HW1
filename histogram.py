from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import cv2
import random

class Histogram(FigureCanvas):
 
    def __init__(self, imsource, parent=None, width=5, height=5, dpi=100):
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

        # Count the occurences

        for i in range(shape[0]):
            for j in range(shape[1]):
                self.data_r[self.img[i,j,2]] += 1
                self.data_g[self.img[i,j,1]] += 1
                self.data_b[self.img[i,j,0]] += 1

        # Plot the bar graphs
        
        ax = self.figure.add_subplot(311)
        ax.bar(arr, self.data_r, width = 0.6, color='red')

        ax = self.figure.add_subplot(312)
        ax.bar(arr, self.data_g, width = 0.6, color='green')
        
        ax = self.figure.add_subplot(313)
        ax.bar(arr, self.data_b, width = 0.6, color='blue')
        
        self.draw()

    def equalize(self,target):

        # Produce the CDF's

        iCDF_r = self.produceCDF(self.data_r, self.img.shape)
        iCDF_g = self.produceCDF(self.data_g, self.img.shape)
        iCDF_b = self.produceCDF(self.data_b, self.img.shape)

        tCDF_r = self.produceCDF(target.data_r, target.img.shape)
        tCDF_g = self.produceCDF(target.data_g, target.img.shape)
        tCDF_b = self.produceCDF(target.data_b, target.img.shape)

        # Define look up tables

        lut_r = np.zeros(256)
        lut_g = np.zeros(256)
        lut_b = np.zeros(256)

        # Fill up look up tables

        for i in range(256):
            
            j = 0
            while(j < 255 and tCDF_r[j] < iCDF_r[i]):
                j += 1
            lut_r[i] = j 

            j = 0
            while(j < 255 and tCDF_g[j] < iCDF_g[i]):
                j += 1
            lut_g[i] = j 

            j = 0
            while(j < 255 and tCDF_b[j] < iCDF_b[i]):
                j += 1
            lut_b[i] = j 
        
        # Create output image

        shape = self.img.shape
        
        output = self.img.copy()

        for i in range(shape[0]):
            for j in range(shape[1]):
                output[i,j,2] = lut_r[output[i,j,2]]
                output[i,j,1] = lut_g[output[i,j,1]]
                output[i,j,0] = lut_b[output[i,j,0]]

        cv2.imwrite("output.png",output)

    def produceCDF(self,data,shape):
        
        # Produce PDF's to create CDF's

        pdf = np.divide(data,float(shape[0]*shape[1]))
        cdf = np.zeros(256)
        cdf[0] = pdf[0]
        for i in range(1,256):
            cdf[i] = pdf[i] + cdf[i-1]
        return cdf
            
