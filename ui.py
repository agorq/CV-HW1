import sys
 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from histogram import Histogram
 
import random
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.left = 0
        self.top = 0
        self.title = 'Histogram Equalization'
        self.width = 1920
        self.height = 1080
        self.inputImagePath = ""
        self.targetImagePath = ""
        self.inputLabel = ""
        self.targetLabel = ""
        self.resultLabel = ""
        self.initUI()
 
    def initUI(self):
        self.inputLabel = QLabel()
        self.inputLabel.setAlignment(Qt.AlignCenter)
        self.targetLabel = QLabel()
        self.targetLabel.setAlignment(Qt.AlignCenter)
        self.resultLabel = QLabel()
        self.resultLabel.setAlignment(Qt.AlignCenter)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.initOptionBar()
 
        central = QWidget()
        hbox = QHBoxLayout(central)

        left = QGroupBox("Input")
        left.width = 640
        center = QGroupBox("Target")
        center.width = 640
        right = QGroupBox("Result")
        right.width = 640
        
        m = Histogram(left, width=5, height=4)
        lvbox = QVBoxLayout(left)
        lvbox.addWidget(self.inputLabel)
        lvbox.addWidget(m)

        cvbox = QVBoxLayout(center)
        cvbox.addWidget(self.targetLabel)
        #cvbox.addWidget(m)

        rvbox = QVBoxLayout(right)
        #rvbox.addWidget(self.inputLabel)
        #rvbox.addWidget(m)

        hbox.addWidget(left)
        hbox.addWidget(center)
        hbox.addWidget(right)

        self.setCentralWidget(central)

        self.show()

    def initOptionBar(self):
        
        OptionBar = self.menuBar()

        FileTab = OptionBar.addMenu('File')
        Equalize = OptionBar.addAction('Equalize Histogram')

        InputAction = QAction('Open Input', self)
        InputAction.triggered.connect(self.openInputImage)
        TargetAction = QAction('Open Target', self)
        TargetAction.triggered.connect(self.openTargetImage)

        FileTab.addAction(InputAction)
        FileTab.addAction(TargetAction)


    def openInputImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "PNG files (*.png)", options=options)
        if fileName:
            inputPixmap = QPixmap(fileName)
            self.inputLabel.setPixmap(inputPixmap)

    def openTargetImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "PNG files (*.png)", options=options)
        if fileName:
            targetPixmap = QPixmap(fileName)
            self.targetLabel.setPixmap(targetPixmap)
 
 

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
