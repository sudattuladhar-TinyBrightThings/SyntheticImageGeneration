import numpy as np
from particle_core import Particle_Core
    
# For purposes of representing the center-points and the centers
class Particle(Particle_Core):
    def __init__(self, params, position):
        # self.image_width = params['image_width']
        # self.image_height = params['image_height']
        self.params = params
        if 'type' not in params.keys():
            raise Exception('Type has to be specified')
        self.type = self.params['type']
        
        #pos = self._generate_position()
        super().__init__(position)

    # def _generate_position(self):
    #     if self.type == 'SPHERE':
    #         self.radiusMean = self.params['radius_mean']
    #         self.radiusSTD = self.params['radius_std']
    #         #minAllowableDistance = 2 * self.radiusMean + 4 * self.radiusSTD
    #         minAllowableDistance = self.params['min_proximity']
    #         px = np.random.uniform(low=minAllowableDistance, high=self.image_width - minAllowableDistance)
    #         py = np.random.uniform(low=minAllowableDistance, high=self.image_height - minAllowableDistance)
    #         return (px, py)
        
    def generate_centroids(self):
        self.num_channels = self.params['num_channels']
        if self.type == 'SPHERE':
            theta = np.linspace(0, 2*np.pi, 15, endpoint=False)
            #self.centroids = 
            print(theta)
    
    def __repr__(self) -> str:
        return f'{self.type} at {self.position}'