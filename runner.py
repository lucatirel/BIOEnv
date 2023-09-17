from creature import *
from ambiente import *
import numpy as np
import random 
from visualization import visualize_3d_heatmap

np.random.seed(42)
random.seed(42)



if __name__ == "__main__":
    organisms = [Bacteria(np.random.randint(0, 30, size=3)) for _ in range(1)] 
    organisms += [Virus(np.random.randint(0, 30, size=3)) for _ in range(0)] 
    organisms += [Fungus(np.random.randint(0, 30, size=3)) for _ in range(0)] 
    
    env = Environment(organisms)
    for i in range(20):
        print(f"STEP {i}")
        print(f"""CREATURES ALIVE:\n
                Bacteria: {len([org for org in env.organisms if (not org.is_dead) and org.name == 'bacteria'])}
                Virus: {len([org for org in env.organisms if (not org.is_dead) and org.name == 'virus'])}
                Fungus: {len([org for org in env.organisms if (not org.is_dead) and org.name == 'fungus'])}
              """)
        env.step()
    visualize_3d_heatmap(env.env_space_temps)
    breakpoint()
    
    
    