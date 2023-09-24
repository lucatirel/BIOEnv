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
    
    def interact(self, env_space_temps=None):
        delta_pos = self.move(env_space_temps)
        return delta_pos
        
    def move(self, *kwargs):
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
        
    # def interact(self, *kwargs):
    #     pass
    
class Virus(Organism):
    def __init__(self, position) -> None:
        super().__init__(position, 'virus')
        
    def interact(self, env_space_temps):
        detection_ranges = rx, ry, rz = self.get_surroundings()
        surrounding_values = self.get_surroundings_values(detection_ranges, env_space_temps)
        
        target_pos = self.get_target_move_pos(detection_ranges, surrounding_values)
        delta_pos = self.move(target_pos=target_pos)
        
        return delta_pos
        
    def move(self, target_pos=None):
        if target_pos:        
            dx, dy, dz = target_pos[0]-self.x, target_pos[1]-self.y, target_pos[2]-self.z
        else:
            dx, dy, dz = super().move()
            
        return dx, dy, dz
    
    def get_surroundings_values(self, detection_ranges, env_space_temps):
        rx, ry, rz = detection_ranges
        return env_space_temps[rx[0]:rx[1], ry[0]:ry[1], rz[0]:rz[1]]
    
    def get_target_move_pos(self, detection_ranges, surrounding_values):
        rx, ry, rz = detection_ranges
        max_index_flat = np.argmax(surrounding_values)
        local_max_index = np.unravel_index(max_index_flat, surrounding_values.shape)        
        global_max_index = (local_max_index[0] + rx[0], local_max_index[1] + ry[0], local_max_index[2] + rz[0])
        return global_max_index
    

class Fungus(Organism):
    def __init__(self, position) -> None:
        super().__init__(position, 'fungus')
        
    # def interact(self):
    #     pass
    
    def move(self, *args):
        return 0, 0, 0
    