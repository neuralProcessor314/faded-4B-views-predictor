import subprocess
import pandas as pd

print("faded-4B-views-predictor CLI. Type /? or /help for help.")
while True:
    cmd = list(input("f4vp-cli>").split()) # split the given command by blankspaces.

    if cmd[0] == 'fetch':
        subprocess.run(["py", "fetch.py"])
    elif cmd[0] == 'predict':
        subprocess.run(["py", "predict.py"])
    elif cmd[0] == 'show':
        subprocess.run(["py", "visualize.py"])

    elif cmd[0] == 'getcfg':
        configs = pd.read_csv("configs.csv", index_col=0) # index_col=0 makes the func read the first column as indexes.
        try: # check if an argument exists. if so then print that config entry.
            cfg_name = cmd[1]
            print(configs.loc[cfg_name, "value"]) # row <cfg_name>, column <value>
        except IndexError: # if no arguments exist, then return all configs.
            print(configs)
    elif cmd[0] == 'setcfg':
        configs = pd.read_csv("configs.csv", index_col=0, dtype='str') # if dtype is unspecified it defaults to int64
                                                                       # and shows some errors cuz cfg_val is str.
        cfg_name = cmd[1]
        cfg_val = cmd[2]
        configs.loc[cfg_name, "value"] = cfg_val
        configs.to_csv("configs.csv")

    elif cmd[0] == 'exit' or cmd[0] == 'quit':
        break