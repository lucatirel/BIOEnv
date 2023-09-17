from ambiente_params import env_grid_size, temp_init_range, temp_decr
import numpy as np

class Cella():
    def __init__(self, temp) -> None:
        self.organisms = []
        self.temp = temp


class Environment():
    def __init__(self, organisms, env_grid_size=env_grid_size, temp_init_range=temp_init_range, temp_decr=temp_decr) -> None:
        self.x_max, self.y_max, self.z_max = env_grid_size
        self.temp_decr = temp_decr
        self.organisms = organisms
        
        self.env_time = 0
        self.env_space_temps = np.random.uniform(temp_init_range[0], temp_init_range[1], env_grid_size)
        self.env_space = {
            f'{x}-{y}-{z}': Cella(self.env_space_temps[x, y, z]) 
            for x in range(self.x_max) 
            for y in range(self.y_max) 
            for z in range(self.z_max)
        }
        
    def reset(self):
        self.env_time = 0
        self.env_space_temps = np.random.uniform(temp_init_range, env_grid_size)
        self.env_space = {
            f'{x}-{y}-{z}': Cella(self.env_space_temps[x, y, z]) 
            for x in range(self.x_max) 
            for y in range(self.y_max) 
            for z in range(self.z_max)
        }
        
    def step(self):
        # Environment change temps
        for x in range(self.x_max):
            for y in range(self.y_max):
                for z in range(self.z_max):
                    dict_key = f"{x}-{y}-{z}"
                    cella = self.env_space[dict_key]
                    if cella.organisms == []:
                        cella.temp += self.temp_decr
                        self.env_space_temps[x,y,z] += self.temp_decr
                                          
        for org in self.organisms:
            # Temperature Increments due to Environment
            if not org.is_dead:
                cell = self.env_space[f"{org.x}-{org.y}-{org.z}"]
                
                cell_temp_is_dangerous = not (cell.temp > org.temp_range[0] and cell.temp < org.temp_range[1])
                if cell_temp_is_dangerous:
                    dmg = 0
                    if cell.temp > org.temp_range[1]:
                        dmg = abs(abs(cell.temp) - abs(org.temp_range[1]))
                    else:
                        dmg = abs(abs(cell.temp) - abs(org.temp_range[0]))
                    org.health -= dmg
            
            if org.health > 0:
                # Temperatures Increments due to Organisms
                self.env_space_temps[org.x, org.y, org.z] += org.temp_incr
                self.env_space[f"{x}-{y}-{z}"].temp += org.temp_incr
                
                # Movement
                org.interact()
                dx, dy, dz = org.move()
                self.update_pos_check(org, dx, dy, dz)
                                
            else:
                org.is_dead = True
        
            
        self.env_time += 1
        return 
    
    def update_pos_check(self, org, dx, dy, dz):
        for movement in [dx, dy, dz]:
            if org.x + dx < self.x_max and org.x + dx > 0:
                org.x += dx
            if org.y + dy < self.y_max and org.y + dy > 0:
                org.y += dy
            if org.z + dz < self.z_max and org.z + dz > 0:
                org.z += dz
                
        
        
# a = Environment(env_grid_size)
# breakpoint()

