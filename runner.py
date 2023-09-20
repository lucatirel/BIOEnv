import time 
from creature import *
from ambiente import *
import numpy as np
import random 
from visualization import visualize_3d_heatmap
import matplotlib.pyplot as plt

np.random.seed(42)
random.seed(42)

if __name__ == "__main__":
    organisms = [Bacteria(np.random.randint(0, 10, size=3)) for _ in range(1)] 
    organisms += [Virus(np.random.randint(0, 10, size=3)) for _ in range(1)] 
    organisms += [Fungus(np.random.randint(0, 10, size=3)) for _ in range(10)] 
    
    env = Environment(organisms)
    
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("3D Heatmap")
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    
    
    for i in range(20):
        print(f"STEP {i}")
        print(f"""CREATURES ALIVE:\n
                Bacteria: {len([org for org in env.organisms if (not org.is_dead) and org.name == 'bacteria'])}
                Virus: {len([org for org in env.organisms if (not org.is_dead) and org.name == 'virus'])}
                Fungus: {len([org for org in env.organisms if (not org.is_dead) and org.name == 'fungus'])}
              """)
        env.step()
        visualize_3d_heatmap(env.env_space_temps, fig, ax)
        # visualize_3d_heatmap(env.env_space_org_density, fig, ax)

        
    
    
    