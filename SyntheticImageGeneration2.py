import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.spatial import distance

class SyntheticImageGenerator():
    def __init__(self):
        np.random.seed(0)
        self._set_initial_parameters()
        self._generate_particle_centroids()
        self._generate_hotspot_points()
        self._initialize_images()
        self._draw_centroids_hotspots()
        self.generate_channels()
    
    def _set_initial_parameters(self):
        # Image Parameters
        self.width = 2048
        self.height = 1536
        # Camera Parameters
        self.C = 15                     # No. of Channels
        # Particle Parameters
        self.N = 10                     # No. of Particles
        self.A = 50                     # Mean Radius of the particles
        self.R = 100                    # Orbital Radius
        #self.S = 5                     # Radius variability in pixels (1 Sigma)
        self.D = 300   

    def _generate_centroid_point(self):
        X = np.random.randint(low = self.A + self.R, high = self.width - (self.A + self.R))
        Y = np.random.randint(low = self.A + self.R, high = self.height - (self.A + self.R))
        return np.array([[X, Y]])
        
    def _generate_particle_centroids(self):
        print('Generating non-overlapping centroids')
        self.centroids = self._generate_centroid_point()
        #for _ in range(1, self.N):
        for _ in range(1, self.N*10):
            if len(self.centroids) >= self.N:              # N number of particles already generated
                break
            centroid = self._generate_centroid_point()
            dist = distance.cdist(centroid, self.centroids, 'euclidean')
            if not np.sum(dist < self.D):   # min distance between centroids criteria met
                self.centroids = np.concatenate((self.centroids, centroid), axis = 0)

    def _generate_hotspot_points(self):
        theta = [np.linspace(0, 2*np.pi, 15, endpoint=False)]
        X = self.R*np.cos(theta)
        Y = self.R*np.sin(theta)
        self.hotspots = []
        for centroid in self.centroids:
            hotspot = np.concatenate((centroid[0] + X , centroid[1] + Y ), axis = 0).T
            self.hotspots.append(hotspot)

    def _initialize_images(self):
        self.channels = [np.zeros((self.height,self.width,3), np.uint8) for _ in range(self.C)]
        self.img_composite = np.zeros((self.height,self.width,3), np.uint8)                                     
        self.img_composite = cv2.bitwise_not(self.img_composite)

    def _draw_centroids_hotspots(self):
        # Centroids
        for centroid in self.centroids:
            self.img_composite = cv2.drawMarker(self.img_composite, (centroid[0], centroid[1]), (0, 0, 255), cv2.MARKER_CROSS, 20, 3)
        # Hotspots
        for hotspot in self.hotspots:
            # Individual circle
            for c in hotspot:
                self.img_composite = cv2.circle(self.img_composite, (int(c[0]), int(c[1])), 20, (0, 0, 0), -1)

    def generate_channels(self):
        for channel in range(self.C):
            for particle in range(self.N):
                cx = self.hotspots[particle][channel][0]
                cy = self.hotspots[particle][channel][1]
                self.channels[channel] = cv2.circle(self.channels[channel], (int(cx), int(cy)), 20, (255, 255, 255), -1)
        

    def get_image(self, channel):
        return self.channels[channel]
    
    def get_composite_image(self):
        return self.img_composite

