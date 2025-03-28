import numpy as np

def signal_intensity(T1, T2, TR, TE, M0=1):
    """Simplified spin echo signal intensity"""
    E1 = np.exp(-TR / T1)
    E2 = np.exp(-TE / T2)
    return M0 * (1 - E1) * E2
