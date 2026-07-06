import pandas as pd
import numpy as np
from funcs import pred_func, to_dhm

# LOADING
print("Loading params.")
params = pd.read_csv("params/pred_params.csv")
[a1p, a2p, a3p, a4p, b1p, b2p] = [params.iloc[i, 1] for i in range(6)] # 'p' after variable names stand for 'predicted'.

#
cfgs = load_cfgs()
pred_precision = int(cfg.loc["pred_precision", "values"])
pred_start = int(cfg.loc["pred_start", "values"])
pred_end = int(cfg.loc["pred_end", "values"])
if pred_precision == 0: