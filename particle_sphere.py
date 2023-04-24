import numpy as np
from particle import Particle
    
# For purposes of representing the center-points and the centers
class Particle_SPHERE(Particle):
    def __init__(self, params, position):
        self.params = params
        self.num_channels = self.params['num_channels']
        self.type = 'SPHERE'
        super().__init__(position)
        self.r = np.random.normal(loc = params['radius_mean'], scale = params['radius_std']) # radius of a hotspot
        
    def _generate_centroids(self):
        self.R = np.repeat(
            np.random.normal(loc = self.params['radial_separation_mean'],scale = self.params['radial_separation_std']), self.num_channels
        )
        noise_angle = np.random.normal(loc = 0, scale = self.params['angular_variation_std'], size = self.num_channels)
        theta = np.linspace(0, 2*np.pi, self.num_channels, endpoint=False) + noise_angle
        X = self.position[0] + self.R*np.cos(theta)
        Y = self.position[1] + self.R*np.sin(theta)
        return np.array((X, Y)).T
    
    def __repr__(self) -> str:
        return f'{self.type} at {self.position}'