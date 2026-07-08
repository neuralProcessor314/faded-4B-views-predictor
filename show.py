import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from funcs import to_mins, pred_func, loadnset_data, load_cfgs

# LOADING
print("Loading params.")
params = pd.read_csv("params/pred_params.csv")
[a1p, a2p, a3p, a4p, b1p, b2p] = [params.iloc[i, 1] for i in range(6)] # 'p' after variable names stand for 'predicted'.

print("Loading configurations.")
show_4b, show_data, show_legends, show_preds = loadnset_data(['show_4b', 'show_data', 'show_legends', 'show_preds'],
                                                             ['bool', 'bool', 'bool', 'bool'])

print("Loading and preprocessing data.")
raw_data, time_tot, views = load_data()

# PREPPING PRED FUNC PLOT
x_space = np.linspace(min(time_tot), max(time_tot), 5000) # linear x data for drawing the predicted func
y_space = pred_func(x_space, a1p, a2p, a3p, a4p, b1p, b2p) # y values for each x points made

# DRAWING
print("Drawing.")
plt.title("Views vs. Time Since June 10, 2026 18:00")
plt.xlabel("time(mins)")
plt.ylabel("views")
if show_4b:
    plt.plot(x_space, [4e9 for _ in range(5000)], color='r', label='4B views')
if show_data:
    plt.scatter(time_tot, views, color='b', label='Data')
if show_preds:
    plt.plot(x_space, y_space, color='y', label='Prediction')
if show_legends: # yes, legend should be the last if statement
    plt.legend()

plt.show()