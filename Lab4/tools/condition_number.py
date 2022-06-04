import numpy as np

def get_number(matrix):
    return np.linalg.norm(matrix) * np.linalg.norm(np.linalg.inv(matrix))