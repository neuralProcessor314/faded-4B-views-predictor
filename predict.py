import pandas as pd
from scipy import optimize # originally used 'from scipy.optimize import curve_fit' but the official guidelines says
                           # to import like this
from funcs import pred_func, load_data, to_mins

save_dir = "params/pred_params.csv"

# DATA PREPROCESSING
print("Loading and processing data.")
raw_data, time_d, time_h, time_m, views = load_data()
time_d -= 10
time_h -= 18
time_tot = to_mins(time_d, time_h, time_m)

# FITTING AND SAVING
print("Fitting.")
params = pd.DataFrame(optimize.curve_fit(pred_func, time_tot, views, maxfev=int(input()))[0])
params.to_csv(save_dir)
print("Saved params at " + save_dir + '.')