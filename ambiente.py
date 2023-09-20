from ambiente_params import env_grid_size, temp_init_range, temp_decr
import numpy as np
from utils import calculate_damage
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
    def __init__(self, organisms, env_grid_size=env_grid_size, temp_init_range=temp_init_range, temp_decr=temp_decr) -> None:
        self.x_max, self.y_max, self.z_max = env_grid_size
        self.temp_decr = temp_decr
        self.organisms = organisms
        
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
            # Temperature Increments due to Environment
            if not org.is_dead:
                cell = self.env_space[f"{org.x}-{org.y}-{org.z}"]
                
                calculate_damage(cell, org)
                # cell_temp_is_dangerous = not (cell.cell_temp > org.temp_range[0] and cell.cell_temp < org.temp_range[1])
                # if cell_temp_is_dangerous:
                #     dmg = 0
                #     if cell.cell_temp > org.temp_range[1]:
                #         dmg = abs(abs(cell.cell_temp) - abs(org.temp_range[1]))
                #     else:
                #         dmg = abs(abs(cell.cell_temp) - abs(org.temp_range[0]))
                #     org.health -= dmg
            
            if org.health > 0:
                # Temperatures Increments due to Organisms
                self.env_space_temps[org.x, org.y, org.z] += org.temp_incr
                
                # Movement
                dx, dy, dz = org.move()
                self.update_pos_check(org, dx, dy, dz)
                                
            else:
                org.is_dead = True
        
            
        self.env_time += 1
        return 
    
    def update_pos_check(self, org, dx, dy, dz):
        old_pos = org.x, org.y, org.z
        for movement in [dx, dy, dz]:
            if org.x + dx < self.x_max and org.x + dx > 0:
                org.x += dx
            if org.y + dy < self.y_max and org.y + dy > 0:
                org.y += dy
            if org.z + dz < self.z_max and org.z + dz > 0:
                org.z += dz
        new_pos = org.x, org.y, org.z
        
        self.env_space_org_density[old_pos] -= 1
        self.env_space_org_density[new_pos] += 1
        
        self.env_space[f"{old_pos[0]}-{old_pos[1]}-{old_pos[2]}"].organisms.remove(org)
        self.env_space[f"{new_pos[0]}-{new_pos[1]}-{new_pos[2]}"].organisms.append(org)
        
        
        
# a = Environment(env_grid_size)
# breakpoint()

