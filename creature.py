import random
from creature_params import org_temp_ranges, org_healths, org_temp_increments

class Organism():
    def __init__(self, position, ) -> None:
        self.x, self.y, self.z = position
        self.is_dead = False
        
    def move(self):
        dx, dy, dz = (random.randint(-1, 1), random.randint(-1, 1), random.randint(-1, 1))
        return dx, dy, dz
    
    
        
        
        

class Bacteria(Organism):
    def __init__(self, position) -> None:
        super().__init__(position)
        self.name = 'bacteria'
        self.temp_range = org_temp_ranges['bacteria']
        self.health = org_healths['bacteria']
        self.temp_incr = org_temp_increments['bacteria']

    def interact(self):
        pass
    
class Virus(Organism):
    def __init__(self, position) -> None:
        super().__init__(position)
        self.name = 'virus'
        self.temp_range = org_temp_ranges['virus']
        self.health = org_healths['virus']
        self.temp_incr = org_temp_increments['virus']
        
    def interact(self):
        pass
        
class Fungus(Organism):
    def __init__(self, position) -> None:
        super().__init__(position)
        self.name = 'fungus'
        self.temp_range = org_temp_ranges['fungus']
        self.health = org_healths['fungus']
        self.temp_incr = org_temp_increments['fungus']

    def interact(self):
        pass
