import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
import cv2 as cv


from particle_sphere import Particle_SPHERE

class Synthetic_Image_Generator():
    HOTSPOT_SIZE = 10

    def __init__(self, params_scene, params_particle) -> None:
        self.params_scene = params_scene
        self.params_particle = params_particle
        self.num_particles = params_scene['num_particles']
        self.num_channels = params_particle['num_channels']
        self.width_scene = params_scene['width_scene']
        self.height_scene = params_scene['height_scene']
        self.min_proximity = params_scene['min_proximity']
        self.radius_mean = self.params_particle['radius_mean']
        self._generate_particles()
        self._initialize_images()
        self._generate_images()

    def _generate_random_position(self):
        min_gap = self.radius_mean
        px = np.random.uniform(low = min_gap, high = self.width_scene - min_gap)
        py = np.random.uniform(low = min_gap, high = self.height_scene - min_gap)
        return (px, py)

    def _generate_particle_position(self):
        position = self._generate_random_position()
        center_points = np.array([position])
        for _ in range(self.num_particles*10):
            if len(center_points) >= self.num_particles:
                self.center_points = center_points
                return True
            center_point = self._generate_random_position()
            dist = distance.cdist([center_point], center_points, 'euclidean')
            if not np.sum(dist < self.min_proximity):   # min distance between centroids criteria met
                center_points = np.vstack((center_points, center_point))
            
        return False
            
    def _generate_particles_position(self):
        # Generate fresh centroids just in case it couldn't be created in first cycle
        for i in range(10):
            #print(f'Cycle: {i}')
            if(self._generate_particle_position()):
                return
        raise Exception('''
                min Proxity criteria could not be met,
                try decreasing num of particles of min proximity
        ''')
    
    def _generate_particles(self):
        self._generate_particles_position()
        self.particles = [Particle_SPHERE(self.params_particle, position = pos) for pos in self.center_points]
        
    def draw_particles(self):
        for idx, particle in enumerate(self.particles):
            plt.scatter(particle.position[0], particle.position[1], marker='x')
            for centroid in particle.centroids:
                plt.scatter(centroid[0], centroid[1], marker='o')
        plt.xlim([0, self.width_scene])
        plt.ylim([0, self.height_scene])
        plt.show()

    def _initialize_images(self):
        self.img_composite = np.zeros((self.height_scene,self.width_scene,3), np.uint8)                                     
        self.img_composite = cv.bitwise_not(self.img_composite)
        self.img_channels = [np.zeros((self.height_scene,self.width_scene,3), np.uint8) for _ in range(self.num_channels)]

    def _generate_image_composite(self):
        for particle in self.particles:
            p_posX = round(particle.position[0])
            p_posY = round(particle.position[1])
            self.img_composite = cv.circle(self.img_composite, (p_posX, p_posY), round(particle.radius), (0, 0, 0), 1)
            self.img_composite = cv.drawMarker(self.img_composite, (p_posX, p_posY), (0, 0, 255), cv.MARKER_CROSS, 20, 3)
            for centroid in particle.centroids:
                self.img_composite = cv.circle(self.img_composite, (round(centroid[0]), round(centroid[1])), self.HOTSPOT_SIZE, (0, 0, 0), -1)

    def _generate_image_channels(self):
        for channel in range(self.num_channels):
            for particle in self.particles:
                cx = particle.centroids[channel][0]
                cy = particle.centroids[channel][1]
                self.img_channels[channel] = cv.circle(self.img_channels[channel], (round(cx), round(cy)), self.HOTSPOT_SIZE, (255, 255, 255), -1)

    def _generate_images(self):
        self._generate_image_composite()
        self._generate_image_channels()

    def get_image_composite(self):
        return self.img_composite
    
    def get_image_channel(self, channel):
        return self.img_channels[channel]


def main():
    import matplotlib.pyplot as plt
    #np.random.seed(100)

    params_scene = {
        # Particles
        'num_particles': 1,
        'min_proximity': 200,

        # Boundary Parameters
        'width_scene': 2048,
        'height_scene':1536,
    }

    params_particle_sphere = {
        # Core-Parameters
        'radius_mean': 75,
        'radius_std': 0.12 * 75,
        'radial_separation_mean': 80,
        'radial_separation_std': 0,

        # Hot-Spot-Parameters
        'num_channels': 15,
        'angular_variation_std': 0, # np.pi/180 * 2,         # 2 degree noise std
    }

    g = Synthetic_Image_Generator(params_scene, params_particle_sphere)
    g.draw_particles()
    

if __name__=='__main__':
    import os
    os.system('clear')
    print('Synthetic Image Generator has started')
    main()
    print('Synthetic Image Generator has ended')


