import numpy as np
from scipy.special import jv

class HotSpot_Structure_SPHERE():
    def __init__(self, size, spread, max_intensity) -> None:
        self.size = size
        self.spread = spread
        self.max_intensity = max_intensity
        self._generate_hotspot_image()

    def _generate_hotspot_image(self):
        x = np.linspace(-self.spread, self.spread, 2*self.size)
        y = np.linspace(-self.spread, self.spread, 2*self.size)
        xv, yv = np.meshgrid(x, y)

        dist = np.sqrt(xv**2 + yv**2)
        #dist[dist > kernel_size] = 0

        # Bessel function of 1st order evaluated at all radial distances from center
        self.img = jv(1, dist)
        self.img = self.img - np.min(self.img)      # making all values positive

        self.img = self.max_intensity/np.max(self.img) * self.img
        self.img[dist > self.spread] = 0

    def plot_hotspot_image(self):
        import matplotlib.pyplot as plt
        plt.imshow(self.img, cmap = plt.get_cmap('gray'))
        plt.show()

def main():
    hs = HotSpot_Structure_SPHERE(
        size = 20,                          # determines the image size: (size, size)
        spread = 16,                        # determines how many annular rings we desire
        max_intensity= 255                  # 255 for 8 bit, 65535 for 8 bit pixel
    )
    hs.plot_hotspot_image()

if __name__=='__main__':
    import os
    os.system('clear')
    main()