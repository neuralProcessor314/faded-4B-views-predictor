import numpy as np
import pandas as pd
from scipy import optimize # originally used 'from scipy.optimize import curve_fit' but the official guidelines says to import like this
from convert import to_dhm, to_mins


# DATA PREPROCESSING
raw_data = pd.read_csv("data/raw_data.csv")
# print(raw_data)

time_d = raw_data.iloc[:, 0]
time_h = raw_data.iloc[:, 1]
time_m = raw_data.iloc[:, 2]
time_tot = to_mins(time_d, time_h, time_m)

views = raw_data.iloc[:, 3]


# FITTING
def pred_func(x, a1, a2, a3, a4, b1, b2):
    omega_1 = 2 * np.pi / 1440  # 1-day = 1440-min period
    omega_2 = 2 * np.pi / 10080  # 1-week = 10080-min period
    return a1*np.sin(omega_1*x + b1) + a2*np.sin(omega_2*x+b2) + a3*x + a4*np.square(x) + 3980917788


print(optimize.curve_fit(pred_func, time_tot, views))