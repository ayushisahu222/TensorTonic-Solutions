import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    # NumPy's .T returns a view (no data copy), just changes how indices map to memory
    # This is very efficient but can cause subtle bugs if you modify the view
    # So use copy to create a copy of A
    B = A.copy()
    return np.transpose(B)
