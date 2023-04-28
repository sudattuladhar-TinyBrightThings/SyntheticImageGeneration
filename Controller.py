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
        #np.random.seed(0)

        params_scene = {
            # Particles
            'num_particles': 10,
            'min_proximity': 200,

            # Boundary Parameters
            'width_scene': 2048,
            'height_scene':1536,

            # Intensity Parameters
            'max_intensity': 255
        }

        params_particle_sphere = {
            # Core-Parameters
            'radius_mean': 75,
            'radius_std': 10,                  # factor * radius_mean

            # Hot-Spot-Parameters
            'num_channels': self.num_channels,
            'angular_variation_std': 0, # np.pi/180 * 2,         # 2 degree noise std
            'radius_hotspot_noise_std_factor': 0.03,
            'hotspot_size': 20,
            'hotspot_intensity_mean': 200,               # 255 for 8 bit, 65535 for 8 bit pixel
            'hotspot_intensity_std': 25,
            'hotspot_vaccilating_bool': True,
            'hotspot_vaccilating_probs': 0.05,
            'hotspot_vaccilating_factor': 0.25,         # controls the hotspot_intensity_mean by this factor while dimming
            'hotspot_type': 'GAUSSIAN_BESSEL',          #  'GAUSSIAN', 'BESSEL', 'GAUSSIAN_BESSEL'
            'hotspot_spread': 16                        # necessary on when adding BESSEL
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
        self.timer.start(250)
        self.show()

        self.saveImages()

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

    def saveImages(self):
        cv.imwrite('Results/Composite.jpg', self.synGenObj.get_image_composite())
        for channel in range(self.num_channels):
            cv.imwrite(f'Results/Channel-{channel+1}.jpg', self.synGenObj.get_image_channel(channel))

def main():
    app = QApplication(sys.argv)
    controller = Controller()
    app.exec()

if __name__ == '__main__':
    import sys
    main()