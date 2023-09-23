import random
from creature_params import org_temp_ranges, org_healths, org_temp_increments, org_interaction_priority, org_sensing_range, org_class_map
from ambiente_params import env_grid_size
import numpy as np

class Organism():
    def __init__(self, position, name) -> None:
        self.name = name
        
        self.name_class_map = org_class_map
        self.temp_range = org_temp_ranges[name]
        self.health = org_healths[name]
        self.temp_incr = org_temp_increments[name]
        self.sensing_range = org_sensing_range[name]
        self.org_interaction_priority = org_interaction_priority[name]
        self.x, self.y, self.z = position
        self.is_dead = False
    
    @classmethod
    def create(cls, position, name):
        class_name = org_class_map.get(name, cls.__name__)  # Get class name from map or default to Organism
        module = __import__(cls.__module__)  # Import the module where this class is defined
        class_ = getattr(module, class_name)  # Get the class from the module
        return class_(position)
    
    def move(self, env_space_temps=None):
        dx, dy, dz = (random.randint(-1, 1), random.randint(-1, 1), random.randint(-1, 1))
        return dx, dy, dz
    
    def get_surroundings(self):
        rx = (max(0, self.x - self.sensing_range), min(self.x + self.sensing_range + 1, env_grid_size[0]))
        ry = (max(0, self.y - self.sensing_range), min(self.y + self.sensing_range + 1, env_grid_size[1]))
        rz = (max(0, self.z - self.sensing_range), min(self.z + self.sensing_range + 1, env_grid_size[2])) 
        # surroundings = env_space_temps[rx[0]:rx[1], ry[0]:ry[1], rz[0]:rz[1]].shape

        return rx, ry, rz
        
    
        

        
        

class Bacteria(Organism):
    def __init__(self, position) -> None:
        super().__init__(position, 'bacteria')
        
    def interact(self):
        pass
    
class Virus(Organism):
    def __init__(self, position) -> None:
        super().__init__(position, 'virus')
        
    def interact(self, env_space_temps):
        pass
        
    def move(self, env_space_temps):        
        rx, ry, rz = self.get_surroundings()
        state_temps = env_space_temps[rx[0]:rx[1], ry[0]:ry[1], rz[0]:rz[1]]
        print(state_temps)
        max_index_flat = np.argmax(state_temps)
        max_index = np.unravel_index(max_index_flat, state_temps.shape)
        dx, dy, dz = max_index[0]-self.x, max_index[1]-self.y, max_index[2]-self.z
        
        if dx == 0 and dy == 0 and dz == 0:
            return super().move()
        
        return dx, dy, dz


class Fungus(Organism):
    def __init__(self, position) -> None:
        super().__init__(position, 'fungus')
        
    def interact(self):
        pass
    
    def move(self, *args):
        return 0, 0, 0
    