import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from funcs import to_mins, pred_func, load_data

# LOADING
print("Loading params.")
params = pd.read_csv("params/pred_params.csv")
[a1p, a2p, a3p, a4p, b1p, b2p, b3p] = [params.iloc[i, 1] for i in range(7)]

print("Loading and preprocessing data.")
raw_data, time_d, time_h, time_m, views = load_data()
time_d -= 10
time_h -= 18
time_tot = to_mins(time_d, time_h, time_m)

# PREPPING PRED FUNC PLOT
x_space = np.linspace(min(time_tot), max(time_tot), 500)
y_space = pred_func(x_space, a1p, a2p, a3p, a4p, b1p, b2p, b3p)

# DRAWING
print("Drawing.")
plt.title("Views vs. Time Since June 10, 2026 18:00")
plt.xlabel("time(mins)")
plt.ylabel("views")
plt.scatter(time_tot, views)
plt.plot(x_space, y_space)
plt.show()