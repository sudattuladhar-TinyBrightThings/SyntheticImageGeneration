import numpy as np
from scipy.spatial import distance
from particle_core import Particle_Core
    
# For purposes of representing the center-points and the centers
class Particle(Particle_Core):
    def __init__(self, params):
        self.image_width = params['image_width']
        self.image_height = params['image_height']
        self.params = params
        if 'type' not in params.keys():
            raise Exception('Type has to be specified')
        self.type = self.params['type']
        
        pos = self._generate_position()
        super().__init__(pos)

    def _generate_position(self):
        if self.type == 'SPHERE':
            self.radiusMean = self.params['radius_mean']
            self.radiusSTD = self.params['radius_std']
            minAllowableDistance = 2 * self.radiusMean + 4 * self.radiusSTD
            px = np.random.uniform(low=minAllowableDistance, high=self.image_width - minAllowableDistance)
            py = np.random.uniform(low=minAllowableDistance, high=self.image_height - minAllowableDistance)
            return (px, py)
        
    def generate_centroids(self):
        self.num_channels = self.params['num_channels']
        if self.type == 'SPHERE':
            pass


    def get_position(self):
        return self.position
    
    def __repr__(self) -> str:
        return f'{self.type} at {self.position}'
    
def main():
    import matplotlib.pyplot as plt
    params = {
        'num_channels': 15,

        # Core-Parameters
        'type': 'SPHERE',
        'radius_mean': 75,
        'radius_std': 0.12 * 75,
        ''
        
        # Boundary Parameters
        'image_width': 2048,
        'image_height':1536,
    }
    
    for i in range(10):
        p_c = Particle(params)
        pos = p_c.get_position()
        plt.scatter(pos[0], pos[1], marker='x')
        print(i, p_c)
    plt.show()

if __name__=='__main__':
    import os
    os.system('clear')
    main()
