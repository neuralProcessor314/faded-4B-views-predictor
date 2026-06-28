import subprocess
import pandas as pd

print("faded-4B-views-predictor CLI. Type ? <none_or_command> or help <none_or_command> for usage help")
while True:
    cmd = list(input("f4vp-cli>").split()) # split the given command by blankspaces.

    if cmd[0] == 'fetch':
        subprocess.run(["py", "fetch.py"])
    elif cmd[0] == 'predict':
        subprocess.run(["py", "predict.py"])
    elif cmd[0] == 'show':
        subprocess.run(["py", "visualize.py"])

    elif cmd[0] == 'get':
        configs = pd.read_csv("configs.csv", index_col=0) # index_col=0 makes the func read the first column as indexes.
        try: # check if an argument exists. if so then print that config entry.
            cfg_name = cmd[1]
            print(configs.loc[cfg_name, "value"]) # row <cfg_name>, column <value>
        except IndexError: # if no arguments exist, then return all configs.
            print(configs)
    elif cmd[0] == 'set':
        configs = pd.read_csv("configs.csv", index_col=0, dtype='str') # if dtype is unspecified it defaults to int64
        cfg_name = cmd[1]                                              # and shows some errors cuz cfg_val is str.
        cfg_val = cmd[2]
        configs.loc[cfg_name, "value"] = cfg_val
        print(configs.loc[cfg_name, "value"])p
        configs.to_csv("configs.csv")

    elif cmd[0] == '?' or  cmd[0] == 'help':
        try:
            if cmd[1] == 'fetch':
                print('fetch             : run fetch.py to fetch data from the sheet then write to data/raw_data.csv.')
            elif cmd[1] == 'predict':
                print('predict           : run predict.py to fit the function to the data.')
            elif cmd[1] == 'show':
                print('show              : run visualize.py to show a plot of the data and the preds.')
            elif cmd[1] == 'get':
                print('get <none_or_cfg> : show the value of a configuration entry. if unspecified show all.')
            elif cmd[1] == 'set':
                print('set <cfg> <value> : set the value of a configuration entry.')
            elif cmd[1] == '?':
                print('? <none_or_cmd>   : show help for a given command. if unspecified show all.')
            elif cmd[1] == 'help':
                print('help <none_or_cmd>: show help for a given command. if unspecified show all.')

        except IndexError:
            print('fetch             : run fetch.py to fetch data from the sheet then write to data/raw_data.csv.')
            print('predict           : run predict.py to fit the function to the data.')
            print('show              : run visualize.py to show a plot of the data and the preds.')
            print('get <none_or_cfg> : show the value of a configuration entry. if unspecified show all.')
            print('set <cfg> <value> : set the value of a configuration entry.')
            print('? <none_or_cmd>   : show help for a given command. if unspecified show all.')
            print('help <none_or_cmd>: identical to ?.')

    elif cmd[0] == 'exit' or cmd[0] == 'quit':
        break