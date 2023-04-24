import numpy as np

# For purposes of implementing physics law later on for movements
class Particle_Core():
    def __init__(self, position):
        #self.mass = params['particle_mass']
        self.position = position                      # same as center-points
        #self.velocity = (0, 0)
        #self.time = 0

    def __repr__(self) -> str:
        return f'Particle at {self.position}'
    
def main():
    p_c = Particle_Core(position=(1,2))
    print(p_c)

if __name__=='__main__':
    import os
    os.system('clear')
    main()