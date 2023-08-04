import sys
import numpy as np
import matplotlib.pyplot as plt

def Correlation_Coefficient(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.corrcoef(x, y)
