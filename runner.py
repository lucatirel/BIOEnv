import time 
from creature import *
from ambiente import Environment
import numpy as np
import random 
from visualization import visualize_3d_heatmap, create_plots

np.random.seed(42)
random.seed(42)

if __name__ == "__main__":
    fig, ax = create_plots()
    
    env = Environment()
    
    visualize_3d_heatmap(env.env_space_org_density, fig, ax)
    for i in range(50):
        print(f"STEP {i}")
        print(f"""CREATURES ALIVE:\n
                Bacteria: {len([org for org in env.organisms if (not org.is_dead) and org.name == 'bacteria'])}
                Virus: {len([org for org in env.organisms if (not org.is_dead) and org.name == 'virus'])}
                Fungus: {len([org for org in env.organisms if (not org.is_dead) and org.name == 'fungus'])}
              """)
        env.step()
        
        visualize_3d_heatmap(env.env_space_temps, fig, ax)
        # visualize_3d_heatmap(env.env_space_org_density, fig, ax)

        
    
    
    