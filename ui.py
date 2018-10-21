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

        self.input = 0
        self.target = 0
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
        Equalize = OptionBar.addAction('Equalize Histogram')

        InputAction = QAction('Open Input', self)
        InputAction.setShortcut('Ctrl+O')
        InputAction.triggered.connect(self.setInputBox)
        TargetAction = QAction('Open Target', self)
        TargetAction.setShortcut('Ctrl+P')
        TargetAction.triggered.connect(self.setTargetBox)
        QuitAction = QAction('Quit', self)
        QuitAction.setShortcut('Ctrl+Q')
        QuitAction.triggered.connect(qApp.quit)


        FileTab.addAction(InputAction)
        FileTab.addAction(TargetAction)
        FileTab.addAction(QuitAction)


    def setInputBox(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "PNG files (*.png)", options=options)
        if fileName:
            layout = self.leftGroup.layout()
            self.input = Histogram(fileName,self.leftGroup)
            
            inputLabel = QLabel()
            inputLabel.setAlignment(Qt.AlignCenter)
            inputPixmap = QPixmap(fileName)
            inputLabel.setPixmap(inputPixmap)

            for i in reversed(range(layout.count())): 
                layout.itemAt(i).widget().setParent(None)
            layout.addWidget(inputLabel)
            layout.addWidget(self.input)
                


    def setTargetBox(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "PNG files (*.png)", options=options)
        if fileName:
            layout = self.centerGroup.layout()
            self.target = Histogram(fileName,self.centerGroup)
            
            targetLabel = QLabel()
            targetLabel.setAlignment(Qt.AlignCenter)
            targetPixmap = QPixmap(fileName)
            targetLabel.setPixmap(targetPixmap)

            for i in reversed(range(layout.count())): 
                layout.itemAt(i).widget().setParent(None)
            layout.addWidget(targetLabel)
            layout.addWidget(self.target)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
