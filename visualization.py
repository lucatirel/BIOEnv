import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import matplotlib.pyplot as plt

def visualize_3d_heatmap(data, fig, ax):    
    ax.clear()
    
    # Ottieni le coordinate x, y, z
    x, y, z = np.indices(data.shape)
    
    # Piatto i dati e le coordinate
    x = x.flatten()
    y = y.flatten()
    z = z.flatten()
    data = data.flatten()
    
    # Crea un grafico scatter 3D con i valori di temperatura come colore
    img = ax.scatter(x, y, z, c=data, cmap='Reds', marker='s', s=100, alpha=0.1)
    
    plt.draw()  # Display the plot
    plt.pause(2)  # Pause for a short interval before continuing

def create_plots():
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("3D Heatmap")
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    
    return fig, ax