import numpy as np
from abc import ABC, abstractmethod

class Particle(ABC):
    def __init__(self, position):
        #self.mass = params['particle_mass']
        self.position = position                      # same as center-points
        #self.velocity = (0, 0)
        #self.time = 0

        self.centroids = self._generate_centroids()

    def __repr__(self) -> str:
        return f'Particle at {self.position}'
    
    @abstractmethod
    def _generate_centroids(self):
        pass