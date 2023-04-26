import cv2 as cv
import os.path
from Main_GUI import Ui_MainWindow
from synthetic_image_generation import Synthetic_Image_Generator
from PyQt5.QtWidgets import (
    QMainWindow, QApplication
)
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QImage
import numpy as np

class Controller(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.num_channels = 15
        np.random.seed(2)

        params_scene = {
            # Particles
            'num_particles': 1,
            'min_proximity': 400,

            # Boundary Parameters
            'width_scene': 2048,
            'height_scene':1536,

            # Intensity Parameters
            'max_intensity': 255
        }

        params_particle_sphere = {
            # Core-Parameters
            'radius_mean': 200,
            'radius_std': 10,                  # factor * radius_mean

            # Hot-Spot-Parameters
            'num_channels': self.num_channels,
            'angular_variation_std': 0, # np.pi/180 * 2,         # 2 degree noise std
            'radius_hotspot_noise_std_factor': 0.03,
            'hotspot_size': 30,
            'hotspot_spread': 16
        }

        self.synGenObj = Synthetic_Image_Generator(params_scene, params_particle_sphere)

        # Main Window
        self._windowMain = Ui_MainWindow()

        img = self.synGenObj.get_image_composite()
        self.showImage(img, self.img)
        img = self.synGenObj.get_image_channel(channel = 0)
        self.showImage(img, self.img0)
        img = self.synGenObj.get_image_channel(channel = 1)
        self.showImage(img, self.img1)

        self.channel = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(100)
        self.show()

    def animate(self):
        img = self.synGenObj.get_image_channel(self.channel)
        self.showImage(img, self.img2)
        self.channel = self.channel + 1
        if self.channel >= self.num_channels:
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