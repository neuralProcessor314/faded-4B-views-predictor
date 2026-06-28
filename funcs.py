import numpy as np
import pandas as pd

def to_mins(d, h, m):
    return 1440 * d + 60 * h + m

def to_dhm(mins):
    d = int(mins/1440)
    mins -= 1440 * d
    h = int(mins/60)
    mins -= 60 * h
    m = mins
    return [d, h, m]

def pred_func(x, a1, a2, a3, a4, b1, b2): # the prediction model
    omega_1 = 2 * np.pi / 1440  # 1-day = 1440-min period
    omega_2 = 2 * np.pi / 10080  # 1-week = 10080-min period
    return a1 * np.sin(omega_1 * x + b1) + a2 * np.sin(omega_2 * x + b2) + a3 * x + a4 * np.square(x) + 3980917788
    # 3980917788 is the viewcount at June 10, 2026 18:11. Close enough to 18:00, so assumed that the video had the
    # same viewcount at 18:00.

def load_data():
    raw_data = pd.read_csv("data/raw_data.csv")
    time_d = raw_data.iloc[:, 0]
    time_h = raw_data.iloc[:, 1]
    time_m = raw_data.iloc[:, 2]
    views = raw_data.iloc[:, 3]

    return raw_data, time_d, time_h, time_m, views

def load_cfg():
    return pd.read_csv("configs.csv", index_col=0) # index_col=0 makes the func read the first column as indexes.