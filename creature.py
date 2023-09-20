import random
from creature_params import org_temp_ranges, org_healths, org_temp_increments, org_interaction_priority, org_sensing_range
from ambiente_params import env_grid_size
class Organism():
    def __init__(self, position, name) -> None:
        self.name = name
        self.temp_range = org_temp_ranges[name]
        self.health = org_healths[name]
        self.temp_incr = org_temp_increments[name]
        self.sensing_range = org_sensing_range[name]
        self.org_interaction_priority = org_interaction_priority[name]

        self.x, self.y, self.z = position
        self.is_dead = False
        
    def move(self):
        dx, dy, dz = (random.randint(-1, 1), random.randint(-1, 1), random.randint(-1, 1))
        return dx, dy, dz
    
    def get_surroundings(self, env_space_temps, env_space_org_density):
        r_x = (min(0, self.x - self.sensing_range), max(self.x + self.sensing_range + 1, env_grid_size[0]))
        r_y = (min(0, self.y - self.sensing_range), max(self.y + self.sensing_range + 1, env_grid_size[1]))
        r_z = (min(0, self.z - self.sensing_range), max(self.z + self.sensing_range + 1, env_grid_size[2])) 
        breakpoint()
        
        return r_x, r_y, r_z
        
    
        

        
        

class Bacteria(Organism):
    def __init__(self, position) -> None:
        super().__init__(position, 'bacteria')
        
    def interact(self):
        pass

class Virus(Organism):
    def __init__(self, position) -> None:
        super().__init__(position, 'virus')
        
    def interact(self):
        pass
    
class Fungus(Organism):
    def __init__(self, position) -> None:
        super().__init__(position, 'fungus')
        
    def interact(self):
        pass
    
    def move(self):
        return 0, 0, 0
    