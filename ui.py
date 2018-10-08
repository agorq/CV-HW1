import sys
 
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QAction, QWidget, QInputDialog, QLineEdit, QFileDialog, QFrame

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
 
import random
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.left = 0
        self.top = 0
        self.title = 'Histogram Equalization'
        self.width = 1280
        self.height = 720
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.initOptionBar()
 
        m = PlotCanvas(self, width=5, height=4)

        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.addWidget(m)

        self.setCentralWidget(widget)

        self.show()

    def initOptionBar(self):
        
        OptionBar = self.menuBar()

        FileTab = OptionBar.addMenu('File')

        InputAction = QAction('Open Input', self)
        InputAction.triggered.connect(self.openImage)
        TargetAction = QAction('Open Target', self)
        TargetAction.triggered.connect(self.openImage)

        FileTab.addAction(InputAction)
        FileTab.addAction(TargetAction)

    def openImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "JPG files (*.jpg)", options=options)
        if fileName:
            print(fileName)
 
 
class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()
 
 
    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
