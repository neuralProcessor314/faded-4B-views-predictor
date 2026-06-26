import numpy as np
import matplotlib.pyplot as plt
import scipy
import pandas as pd

data = pd.read_csv("data/raw_data.csv")

def pred_func(x, a1, a2, a3, a4, a5, b1, b2):
    return a1*np.sin(a2*x + b1) + a2*x + a3*np.square(x) + a4*np.exp(a5*x) + b2

