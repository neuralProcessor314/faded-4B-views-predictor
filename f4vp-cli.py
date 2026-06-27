import subprocess

print("FADED-4B-VIEWS-PREDICTOR CLI. Type /? for help.")
while True:
    cmd = list(input("f4vp-cli>").split())
    if cmd[0] == '/fetch':
        subprocess.run(["py", "fetch.py"])
    elif cmd[0] == '/predict':
        try:
            idx_iter = cmd.index("--iter")
            subprocess.run(["py", "predict.py"])
            subprocess.run([str(cmd[idx_iter + 1])])
        except ValueError:
            subprocess.run(["py", "predict.py", "1200"])
    elif cmd[0] == '/show':
        subprocess.run(["py", "visualize.py"])
    elif cmd[0] == '/exit':
        break
