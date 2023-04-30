import numpy as np
import cv2 as cv
from scipy.special import jv

class HotSpot_Structure_SPHERE():
    def __init__(self, params) -> None:
        self.params = params
        self.size = params['hotspot_size']
        self.type = params['hotspot_type']
        if self.type == 'BESSEL' or self.type == 'GAUSSIAN_BESSEL':
            self.spread = params['hotspot_spread']
        self.generate_hotspot_image()

    def _calc_distances(self, x, y):
        xv, yv = np.meshgrid(x, y)
        self.dist = np.sqrt(xv**2 + yv**2)

    def _generate_random_max_intensity(self):
        hotspot_intensity_mean = self.params['hotspot_intensity_mean']
        if self.params['hotspot_vaccilating_bool'] == True:
            p = self.params['hotspot_vaccilating_probs']
            factor = np.random.choice([self.params['hotspot_vaccilating_factor'], 1], p = [p, 1-p])
            hotspot_intensity_mean = hotspot_intensity_mean * factor

        max_intensity = np.random.normal(loc = hotspot_intensity_mean, scale = self.params['hotspot_intensity_std'])
        max_intensity = 255 if max_intensity > 255 else max_intensity
        max_intensity = 0 if max_intensity < 0 else max_intensity
        return max_intensity
    
    def _generate_gaussian_hotspot(self):
        x = np.linspace(-self.size, self.size, 2*self.size)
        y = np.linspace(-self.size, self.size, 2*self.size)
        self._calc_distances(x, y)
        self.dist[self.dist > 0.9 * self.size] = self.size
        max_intensity = self._generate_random_max_intensity()
        hotspot_img = cv.normalize(self.dist, None, 0, max_intensity, cv.NORM_MINMAX)
        hotspot_img = max_intensity - hotspot_img
        return hotspot_img

    def _generate_bessel_hotspot(self):
        x = np.linspace(-self.spread, self.spread, 2*self.size)
        y = np.linspace(-self.spread, self.spread, 2*self.size)
        self._calc_distances(x, y)
        #self.dist[self.dist > 0.9 * self.size] = self.size
        hotspot_img = jv(0, self.dist)
        max_intensity = self._generate_random_max_intensity()
        hotspot_img = cv.normalize(hotspot_img, None, 0, max_intensity, cv.NORM_MINMAX)
        hotspot_img[self.dist > self.spread] = 0
        return hotspot_img
        #self.hotspot_img = cv.add(self.hotspot_img, self.hotspot_bessel, dtype=cv.CV_64F)

    def _generate_gaussian_bessel_hotspot(self):
        max_intensity = self._generate_random_max_intensity()
        #hotspot_img = cv.add(self._generate_gaussian_hotspot(), self._generate_bessel_hotspot(), dtype = cv.CV_8U)
        ## hotspot_img = cv.normalize(hotspot_img, None, 0, max_intensity, cv.NORM_MINMAX)
        rand_num = np.random.uniform()
        hotspot_img = rand_num*self._generate_bessel_hotspot() + (1 - rand_num)*self._generate_gaussian_hotspot()
        hotspot_img = cv.normalize(hotspot_img, None, 0, max_intensity, cv.NORM_MINMAX)
        return hotspot_img
        
    def generate_hotspot_image(self):
        if self.type == 'GAUSSIAN':
            return self._generate_gaussian_hotspot()
        elif self.type == 'BESSEL':
            return self._generate_bessel_hotspot()
        elif self.type == 'GAUSSIAN_BESSEL': 
            return self._generate_gaussian_bessel_hotspot()
        else:
            raise Exception('Type argument not valid')
        return self.hotspot_img

def main():
    import matplotlib.pyplot as plt
    params = {
            # Hot-Spot-Parameters
            'hotspot_size': 20,
            'hotspot_intensity_mean': 200,               # 255 for 8 bit, 65535 for 8 bit pixel
            'hotspot_intensity_std': 25,
            'hotspot_vaccilating_bool': True,
            'hotspot_vaccilating_probs': 0.05,
            'hotspot_vaccilating_factor': 0.25,         # controls the hotspot_intensity_mean by this factor while dimming
            'hotspot_type': 'GAUSSIAN_BESSEL',          #  'GAUSSIAN', 'BESSEL', 'GAUSSIAN_BESSEL'
            'hotspot_spread': 20                        # necessary on when adding BESSEL
        }

    hs = HotSpot_Structure_SPHERE(params)
    hotspot_img = hs.generate_hotspot_image()
    plt.imshow(hotspot_img, cmap = plt.get_cmap('gray'))
    plt.show()

if __name__=='__main__':
    import os
    os.system('clear')
    main()