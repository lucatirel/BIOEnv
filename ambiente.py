from ambiente_params import env_grid_size, temp_init_range, temp_decr, env_organisms
from creature import Organism
import numpy as np
from utils import organism_temp_damage

class Cella():
    def __init__(self, indices, env_space_temps, env_space_org_density) -> None:
        self.x, self.y, self.z = indices
        
        self.env_space_org_density = env_space_org_density
        self.env_space_temps = env_space_temps
        
        self.organisms = []

    @property
    def cell_temp(self):
        return self.env_space_temps[self.x, self.y, self.z]
    
    @property
    def cell_org_density(self):
        return self.env_space_org_density[self.x, self.y, self.z]


class Environment():
    def __init__(self, env_grid_size=env_grid_size, temp_init_range=temp_init_range, temp_decr=temp_decr) -> None:
        self.x_max, self.y_max, self.z_max = env_grid_size
        self.temp_decr = temp_decr
        self.organisms = sorted([
            Organism.create(np.random.randint(0, env_grid_size[0], size=3), org_type) 
            for org_type, count in env_organisms.items() 
            for _ in range(count)
        ], key=lambda x: x.org_interaction_priority, reverse=True,
        )
        
        self.env_time = 0
        self.env_space_temps = np.random.uniform(temp_init_range[0], temp_init_range[1], env_grid_size)
        self.env_space_org_density = np.zeros(shape=(self.x_max, self.y_max, self.z_max))

        self.env_space = {
            f'{x}-{y}-{z}': Cella((x,y,z), self.env_space_temps, self.env_space_org_density) 
            for x in range(self.x_max) 
            for y in range(self.y_max) 
            for z in range(self.z_max)
        }
        
        for org in self.organisms:
            self.env_space[f'{org.x}-{org.y}-{org.z}'].organisms.append(org)
            self.env_space_org_density[org.x, org.y, org.z] += 1
        
        
    def step(self):
        # Environment change temps
        self.env_space_temps = np.where(self.env_space_org_density == 0, self.env_space_temps + self.temp_decr, self.env_space_temps)

        for org in self.organisms:
            # Temperature Deltas due to Environment
            if not org.is_dead:
                cell = self.env_space[f"{org.x}-{org.y}-{org.z}"]
                organism_temp_damage(cell, org)
            
            if org.health > 0:
                # Temperatures Deltas due to Organisms
                self.env_space_temps[org.x, org.y, org.z] += org.temp_incr
                
                # Movement                
                print(id(org), org.name, org.x, org.y, org.z)
                delta_pos = org.interact(self.env_space_temps)
                self.update_org_position(org, *delta_pos)
            
            else:
                org.is_dead = True
        
        self.env_time += 1
        return 
    
    def update_org_position(self, org, dx, dy, dz):
        old_pos = org.x, org.y, org.z
        
        if org.x + dx < self.x_max and org.x + dx >= 0:
            org.x += dx
        if org.y + dy < self.y_max and org.y + dy >= 0:
            org.y += dy
        if org.z + dz < self.z_max and org.z + dz >= 0:
            org.z += dz
            
        new_pos = org.x, org.y, org.z
        
        self.env_space_org_density[old_pos] -= 1
        self.env_space_org_density[new_pos] += 1

        self.env_space[f"{old_pos[0]}-{old_pos[1]}-{old_pos[2]}"].organisms.remove(org)
        self.env_space[f"{new_pos[0]}-{new_pos[1]}-{new_pos[2]}"].organisms.append(org)
        
    