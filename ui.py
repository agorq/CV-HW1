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

        self.leftGroup = QGroupBox("Input")
        QVBoxLayout(self.leftGroup)

        self.centerGroup = QGroupBox("Target")
        QVBoxLayout(self.centerGroup)

        self.rightGroup = QGroupBox("Result")
        QVBoxLayout(self.rightGroup)

        #Had to use an array for histogram storage because of impossibility of passing references in lambda function used in connections
        self.img=[0,0,0]
        
        self.initUI()
 
    def initUI(self):
        resultLabel = QLabel()
        resultLabel.setAlignment(Qt.AlignCenter)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.initOptionBar()
 
        central = QWidget()
        hbox = QHBoxLayout(central)

        hbox.addWidget(self.leftGroup)
        hbox.addWidget(self.centerGroup)
        hbox.addWidget(self.rightGroup)

        self.setCentralWidget(central)

        self.show()

    def initOptionBar(self):
        
        OptionBar = self.menuBar()

        FileTab = OptionBar.addMenu('File')
        
        EqualizeAction = QAction('Equalize Histogram',self)
        EqualizeAction.triggered.connect(self.equalizeHistogram)
        OptionBar.addAction(EqualizeAction)

        InputAction = QAction('Open Input', self)
        InputAction.triggered.connect(lambda: self.setHistogram(self.leftGroup,0))
        FileTab.addAction(InputAction)

        TargetAction = QAction('Open Target', self)
        TargetAction.triggered.connect(lambda: self.setHistogram(self.centerGroup,1))
        FileTab.addAction(TargetAction)

    def setHistogram(self,targetBox,targetHistogram):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "PNG files (*.png)", options=options)
        
        if fileName:
            layout = targetBox.layout()
            self.img[targetHistogram] = Histogram(fileName,targetBox)
            
            label = QLabel()
            label.setAlignment(Qt.AlignCenter)
            pixmap = QPixmap(fileName)
            label.setPixmap(pixmap)

            for i in reversed(range(layout.count())): 
                layout.itemAt(i).widget().setParent(None)
            layout.addWidget(label)
            layout.addWidget(self.img[targetHistogram])
                
    def equalizeHistogram(self):
        self.img[0].equalize(self.img[1])
        layout = self.rightGroup.layout()
        self.img[2] = Histogram("./output.png",self.rightGroup)
            
        label = QLabel()
        label.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("./output.png")
        label.setPixmap(pixmap)

        for i in reversed(range(layout.count())): 
            layout.itemAt(i).widget().setParent(None)
        layout.addWidget(label)
        layout.addWidget(self.img[2])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
