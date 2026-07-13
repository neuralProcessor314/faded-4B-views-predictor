import pandas as pd
import numpy as np
from funcs import pred_func, to_dhm, loadnset_cfgs

# LOADING
print("Loading params.")
params = pd.read_csv("params/pred_params.csv")
[a1p, a2p, a3p, a4p, b1p, b2p] = [params.iloc[i, 1] for i in range(6)] # 'p' after variable names stand for 'predicted'.

print('Loading configurations.')
pred_precision, pred_start, pred_end = loadnset_cfgs(['pred_start', 'pred_end', 'pred_precision'], ['int', 'int', 'int'])

x = np.linspace(pred_start,pred_end,pred_precision+1) # divide linear space equally by pred_precision fragments.
print(pred_precision)
# PREDICTING
print('Predicting.')
yp = pred_func(x, a1p, a2p, a3p, a4p, b1p, b2p) # predict the y values.

final_idx = 0
for i in range(pred_precision):
    if yp[i] >= 4e9: final_idx = i; break

hit_upperbound = to_dhm(x[final_idx] + 10*3600 + 18*60) # will hit 4b views between this time..
hit_lowerbound = to_dhm(x[final_idx-1] + 10*3600 + 18*60) # ..and this time.
# 10*3600 and 18*60 are added to account for the reference time.

# cuz the video will hit 4B no earlier than July, subtract each date by 30 to get July xx instead of June xx.
hit_upperbound[0] -= 30
hit_lowerbound[0] -= 30

hub_d = hit_upperbound[0]
hub_h = hit_upperbound[1]
hub_m = hit_upperbound[2]

hlb_d = hit_lowerbound[0]
hlb_h = hit_lowerbound[1]
hlb_m = hit_lowerbound[2]

print('Faded will hit 4B views between July', str(hlb_d)+', 2026', str(hlb_h)+':'+str(np.floor(hlb_m)), 'and July', str(hub_d)+', 2026', str(hub_h)+':'+str(np.ceil(hub_m))+'.')