#bfs
#%%
import numpy as np
#%%
def bfs(graph, start):
    graph = np.array(graph)
    start = np.array(start)
    queue = [start]
    
    return graph, start