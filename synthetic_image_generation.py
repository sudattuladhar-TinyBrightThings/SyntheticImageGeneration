import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance


from particle import Particle

class Synthetic_Image_Generator():
    def __init__(self, params_scene, params_particle) -> None:
        self.params_scene = params_scene
        self.params_particle = params_particle
        self.num_particles = params_scene['num_particles']
        self.width_scene = params_scene['width_scene']
        self.height_scene = params_scene['height_scene']
        self.min_proximity = params_scene['min_proximity']
        self._generate_particles()

    def _generate_random_position(self):
        px = np.random.uniform(low=0, high=self.width_scene)
        py = np.random.uniform(low=0, high=self.height_scene)
        return (px, py)

    def _generate_particle_position(self):
        position = self._generate_random_position()
        center_points = np.array([position])
        for _ in range(self.num_particles*10):
            center_point = self._generate_random_position()
            dist = distance.cdist([center_point], center_points, 'euclidean')
            if not np.sum(dist < self.min_proximity):   # min distance between centroids criteria met
                center_points = np.vstack((center_points, center_point))
            if len(center_points) >= self.num_particles:
                self.center_points = center_points
                return True
        return False
            
    def _generate_particles_position(self):
        # Generate fresh centroids just in case it couldn't be created in first cycle
        for i in range(10):
            if(self._generate_particle_position()):
                return
        raise Exception('''
                min Proxity criteria could not be met,
                try decreasing num of particles of min proximity
        ''')
    
    def _generate_particles(self):
        self._generate_particles_position()
        self.particles = [Particle(self.params_particle, position = pos) for pos in self.center_points]
        
        
        for idx, particle in enumerate(self.particles):
            plt.scatter(particle.position[0], particle.position[1], marker='x')
            print(idx, particle)
        plt.show()

def main():
    import matplotlib.pyplot as plt

    params_scene = {
        # Particles
        'num_particles': 25,
        'min_proximity': 200,

        # Boundary Parameters
        'width_scene': 2048,
        'height_scene':1536,
    }

    params_particle = {
        # Core-Parameters
        'type': 'SPHERE',
        'radius_mean': 75,
        'radius_std': 0.12 * 75,
        'radial_separation_mean': 100,
        'radial_separation_std': 10,

        # Hot-Spot-Parameters
        'num_channels': 15,
        'angular_variation_std': 5,
    }

    g = Synthetic_Image_Generator(params_scene, params_particle)
    

if __name__=='__main__':
    import os
    os.system('clear')
    print('Synthetic Image Generator has started')
    main()
    print('Synthetic Image Generator has ended')


