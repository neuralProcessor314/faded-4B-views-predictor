import pandas as pd
from scipy import optimize # originally used 'from scipy.optimize import curve_fit' but the official guidelines says
                           # to import like this
from funcs import pred_func, load_data, load_cfgs, to_mins, loadnset_cfgs

save_dir = "params/pred_params.csv"

# DATA PREPROCESSING
print("Loading and processing data.")
raw_data, time_tot, views = load_data()

# for i in range(66):
#     print(time_tot.iloc[i], ',', views.iloc[i])
# code used to manually convert the datetime format of raw_data.csv

# LOADING CONFIGURATIONS.
print("Loading configurations.")
max_iters = loadnset_cfgs(['max_iters'], ['int'])[0]

# FITTING AND SAVING
print("Fitting.")
params = pd.DataFrame(optimize.curve_fit(pred_func, time_tot, views, maxfev=max_iters)[0])
params.to_csv(save_dir)
print("Saved params at " + save_dir + '.')