import cv2 as cv
import os.path
from Main_GUI import Ui_MainWindow
from SyntheticImageGeneration2 import SyntheticImageGenerator
from PyQt5.QtWidgets import (
    QMainWindow, QApplication
)
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QImage

class Controller(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.synGenObj = SyntheticImageGenerator()

        # Main Window
        self._windowMain = Ui_MainWindow()

        img = self.synGenObj.get_composite_image()
        self.showImage(img, self.img)
        img = self.synGenObj.get_image(channel = 0)
        self.showImage(img, self.img0)
        img = self.synGenObj.get_image(channel = 1)
        self.showImage(img, self.img1)

        self.channel = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(50)
        self.show()

    def animate(self):
        img = self.synGenObj.get_image(self.channel)
        self.showImage(img, self.img2)
        self.channel = self.channel + 1
        if self.channel >= 15:
            self.channel = 0

    def showImage(self, img, imglabel):
        if len(img.shape) == 3:
            height, width, channel = img.shape
            bytesPerLine = 3 * width
            qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        else: 
            height, width = img.shape
            bytesPerLine = 1 * width
            qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_Indexed8)
        imglabel.setPixmap(QPixmap(qImg))


def main():
    app = QApplication(sys.argv)
    controller = Controller()
    app.exec()

if __name__ == '__main__':
    import sys
    main()