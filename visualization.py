import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

def visualize_3d_heatmap(data):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Ottieni le coordinate x, y, z
    x, y, z = np.indices(data.shape)
    
    # Piatto i dati e le coordinate
    x = x.flatten()
    y = y.flatten()
    z = z.flatten()
    data = data.flatten()
    
    # Crea un grafico scatter 3D con i valori di temperatura come colore
    img = ax.scatter(x, y, z, c=data, cmap='Greys', marker='s', s=5, alpha=0.1)
    
    ax.set_title("3D Heatmap")
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    
    # Aggiungi una colorbar
    fig.colorbar(img)
    
    plt.show()
