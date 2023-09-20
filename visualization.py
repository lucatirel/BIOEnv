import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

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
    img = ax.scatter(x, y, z, c=data, cmap='Reds', marker='s', s=200, alpha=0.2)
    
    plt.draw()  # Display the plot
    plt.pause(1)  # Pause for a short interval before continuing

