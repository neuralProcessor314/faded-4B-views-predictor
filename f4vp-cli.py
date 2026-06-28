import subprocess
import pandas as pd

print("faded-4B-views-predictor. Type ? <none_or_command> or help <none_or_command> for usage help.")
while True:
    cmd = list(input("f4vp-cli>").split()) # split the given command by blankspaces.
    if len(cmd) == 0: continue # to avoid errors when no command is given.

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
        print(configs.loc[cfg_name, "value"])
        configs.to_csv("configs.csv")

    elif cmd[0] == '?' or  cmd[0] == 'help':
        usages = pd.read_csv("usages.csv", index_col=0) # load the usage helps file.
        try: print(usages.loc[cmd[1],"."])
        except IndexError: # if cmd[1] does not exist; i.e. when no additional arguments  provided.
            print('')
            for i in range(usages.shape[0]): print(usages.iloc[i,0])
            print('')
        except KeyError: print(cmd[1], "is not a valid command.") # if cmd[1] is not a valid index.

    elif cmd[0] == 'exit' or cmd[0] == 'quit' or cmd[0] == 'bye' or cmd[0] == 'seeyou' or cmd[0] == 'seeya':
        print("Bye!")
        break