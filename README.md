*You were the shadow of my light*  
**ALAN WALKER - FADED**

## Overview
A machine learning script to predict the time at which Alan Walker's Faded would hit four billion views on YouTube. NO AI SLOP :D

Why did I made this?
- FADED'S GONNA HIT A WHOLE FOUR BILLION VIEWS SOON AND I WANT TO PREDICT WHEN IT IS, SO THAT I CAN CELEBRATE! THAT'S ALL.

## How it works
### Recording Views
I visit YouTube at random times to check how much views *Faded* has at that moment. As it is impractical and meaningless to record the time down to the precise seconds, I cut the seconds and write times down to minutes on my Google Sheets spreadsheet. As of June 2026, the sheet has the following structure:
|time(D)|time(H)|time(M)|views|timeSinceRef|
|-------|-------|-------|-----|------------|
|10|18|11|3980917788|11|
|...|...|...|...|...|

Where,  
<dl>
<dt>time(D)</dt>
<dd>The date part of the timestamp. All entries in June as of June 26, 2026.</dd>

<dt>time(H)</dt>
<dd>The hour part of the timestamp. 0~23.</dd>

<dt>time(M)</dt>
<dd>The minute part of the timestamp.</dd>

<dt>views</dt>
<dd>view count as of the timestamp.</dd>

<dt>timeSinceRef</dt>
<dd>time elapsed since June 10, 2026 18:00. Deprecated; Although the current reference time is identical, the dhm-to-minutes conversion is done locally.</dd>
</dl>
All times are in KST(UTC+9).

### Fetching Data
Using the Google Sheets API, fetch.py fetches the current sheet and stores the D/H/M/views columns in .csv format. The code is heavily based on the example in [Google Sheets API Docs](https://developers.google.com/workspace/sheets/api/guides/concepts).

### Regress!
Using scipy, fit.py performs a multivariable regression with the following model:
> a<sub>1</sub>sin(omega<sub>1</sub>x + b<sub>1</sub>) + a<sub>2</sub>sin(omega<sub>2</sub>x + b<sub>2</sub>) + a<sub>3</sub>x<sup>2</sup> + a<sub>4</sub> + 3980917788

Where,  
<dl>
<dt>two sins</dt>
<dd>account for the periodic fluctuation related to the time of the day/week. UPDATE: now has fixed angular velocities, omega_1 and omega_2, to force them to work as desired.</dd>

<dt>exponential(DELETED)</dt>
<dd>accounts for the gradual increase in popularity due to Faded's views getting closer to 4 billion. Deleted as I couldn't manage to make it converge.</dd>

<dt>x squared</dt>
<dd>because it looks similar to the exponential.</dd>

<dt>x</dt>
<dd>constant baseline rate</dd>

<dt>3980917788</dt>
<dd>viewcount at June 10, 2026 18:11 UTC+9, which is pretty close to the reference time and can be approximated, considering YouTube's viewcount updates are not immediate; See https://www.youtube.com/watch?v=oIkhgagvrjI.</dd>
</dl>

### Visualizing Results
Used matplotlib. Shows the viewcount from June 10, 2026 18:11 to latest.

## Other Features

### CLI
f4vp-cli.py hosts the CLI. The CLI currently supports the following commands:
<dl>
<dt>fetch</dt>
<dd>run fetch.py to fetch data from the sheet then write to data/raw_data.csv.</dd>
<dt>fit</dt>
<dd>run fit.py to fit the function to the data.</dd>
<dt>show</dt>
<dd>run show.py(previously visualize.py) to show a plot of the data and the preds.</dd>
<dt>predict</dt>
<dd>run predict.py to calculate the time that Faded will hit 4B views.
<dt>get</dt>
<dd>show the value of a configuration entry. if unspecified show all.</dd>
<dt>set</dt>
<dd>set the value of a configuration entry.</dd>
<dt>?, help</dt>
<dd>show help for a given command. if unspecified show all.</dd>
<dt>exit, quit, seeyou, seeya</dt>
<dd>exit the CLI.</dd>
</dl>

### configs.csv
configs.csv is where all the settings live. Initially intended to incorporate arguments to set values such as the max iterations for curve_fit, but I couldn't figure out a way to start a python process while inputting something there, so I decided to go for a separate configurations file. It includes the following configuration options:
<dl>
<dt>max_iters</dt>
<dd>maximum # of iterations during fitting.</dd>
<dt>pred_start</dt>
<dd>(minutes) start of prediction scope.</dd>
<dt>pred_end</dt>
<dd>(minutes) end of prediction scope.</dd>
<dt>pred_precision</dt>
<dd>number of divisions of the prediction scope. It is NOT the number of points, but the number of FRAGMENTS i.e. np.linspace(pred_start, pred_end, pred_precision+1) will be run.</dd>
<dt>show_4b</dt>
<dd>(NOT YET FUNCTIONAL) whether or not to show the 4 billion views target in the plot.</dd>
<dt>show_data</dt>
<dd>(NOT YET FUNCTIONAL) whether or not to show the datapoints in the plot.</dd>
<dt>show_legends</dt>
<dd>(NOT YET FUNCTIONAL) whether or not to show the legends in the plot.</dd>
<dt>show_preds</dt>
<dd>(NOT YET FUNCTIONAL) whether or not to show the prediction graph in the plot.</dd>
<dt>target</dt>
<dd>(NOT YET FUNCTIONAL) the target viewcount.</dd>
</dl>
If you wish to use the default value set inside the code, simply set the desired config value to 0.

format:
|<None>|value|
|------|-----|
|name1|value1|
|...|...|
note that the names are *indexes*, not entries.

### do_not_push
You may have seen this folder attributed in some of the codes. Inside there is the API information including client secret, etc. As it should not be leaked online, the content is stored locally in the developer's computer, and the folder is included in .gitignore.

### usages.csv
usages.csv includes the contents that *help* or *?* will output. It has the following format:
|<None>|.|
|------|---|
|func1|desc1|
|...|...|
note that the function names are *indexes*, not entries.

## Dependencies
- googleapiclient
- google.auth.transport.requests
- google.oauth2.credentials
- google_auth_oauthlib
- matplotlib.pyplot
- numpy
- pandas
- scipy.optimize
- subprocess

## References
- [Google Sheets API Docs](https://developers.google.com/workspace/sheets/api/guides/concepts)
- [Markdown Guide's cheatsheet](https://www.markdownguide.org/cheat-sheet/)
- [Choose a License](https://choosealicense.com/)
- [Pandas API Reference](https://pandas.pydata.org/pandas-docs/stable/reference/)
- [Python 3.14.6 Documentation](https://docs.python.org/3/)
- [SciPy API Reference](https://docs.scipy.org/doc/scipy/reference/)
- [Numberphile's Video](https://www.youtube.com/watch?v=oIkhgagvrjI)
- [Pandas User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/)
- [Using Matplotlib](https://matplotlib.org/stable/users/index.html)
- [YouTube Data API](https://developers.google.com/youtube/v3/)
- ...and many Stack Overflow answers of course.

