import numpy as np

def euclidean_distance(x, y):
    """
    Returns: float, the Euclidean distance between x and y.
    """
    if len(x) != len(y):
        raise ValueError("Vectors must be of same length")
        
    x_nump = np.array(x)
    y_nump = np.array(y)
    ans = 0
    
    for i in range(len(x_nump)):
        ans = ans + np.square(x_nump[i]-y_nump[i])

    return np.sqrt(ans)
    