# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# N = 15
# print(np.random.uniform(low = 0, high = 1, size = (N, 2)))
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance

class SyntheticImageGenerator():
    def __init__(self):
        np.random.seed(0)
        self._set_initial_parameters()
        self._generate_particle_centroids()
        self._generate_hotspot_points()
        self._show_particles()

    def _set_initial_parameters(self):
        # Image Parameters
        self.width = 2048
        self.height = 1536
        # Camera Parameters
        self.C = 15                                     # No. of Channels
        # Particle Parameters
        self.N = 10                                               # No. of Particles
        self.A = 50                                                # Mean Radius of the particles
        self.R = 100                                               # Orbital Radius
        #self.S = 5                                                # Radius variability in pixels (1 Sigma)
        self.D = 300                                              # Density: minimum distance between centers

    def _generate_centroid_point(self):
        X = np.random.randint(low = self.A + self.R, high = self.width - (self.A + self.R))
        Y = np.random.randint(low = self.A + self.R, high = self.height - (self.A + self.R))
        return np.array([[X, Y]])
        
    def _generate_particle_centroids(self):
        print('Generating non-overlapping centroids')
        self.centroids = self._generate_centroid_point()
        #for _ in range(1, self.N):
        for _ in range(1, self.N*10):
            if len(self.centroids) >= self.N:                       # N number of particles already generated
                break
            centroid = self._generate_centroid_point()
            dist = distance.cdist(centroid, self.centroids, 'euclidean')
            if not np.sum(dist < self.D):   # min distance criteria met
                self.centroids = np.concatenate((self.centroids, centroid), axis = 0)

    def _generate_hotspot_points(self):
        theta = [np.linspace(0, 2*np.pi, 15, endpoint=False)]
        X = self.R*np.cos(theta)
        Y = self.R*np.sin(theta)
        self.hotspots = []
        for centroid in self.centroids:
            print('Centroid', centroid)
            hotspot = np.concatenate((centroid[0] + X , centroid[1] + Y ), axis = 0).T
            self.hotspots.append(hotspot)

    def _show_particles(self):
        plt.scatter(x = self.centroids[:,0], y = self.centroids[:,1], marker='x')
        for hotspot in self.hotspots:
            plt.scatter(x = hotspot[:,0], y = hotspot[:,1], marker='*')
        plt.xlim([0, self.width])
        plt.ylim([0, self.height])
        plt.show()

        





def main():
    synGenObj = SyntheticImageGenerator()

if __name__=='__main__':
    import os
    os.system('clear')
    main()

