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
<dd>time elapsed since June 10, 2026 18:00. Deprecated; The current reference time is June 10, 2026 18:11.</dd>
</dl>
All times are in KST(UTC+9).

### Fetching Data
Using the Google Sheets API, fetch.py fetches the current sheet and stores the D/H/M/views columns in .csv format. The code is heavily based on the example in [Google Sheets API Docs](https://developers.google.com/workspace/sheets/api/guides/concepts).

### Regress!
Using scipy, main.py performs a multivariable regression with the following model:
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
<dd>viewcount at June 10, 2026 18:11 UTC+9, which is the reference time.</dd>
</dl>

### Visualizing Results
Will use matplotllib. To be added.

### CLI
Yes, it has a CLI! To be added.

## Dependencies
- googleapiclient
- google.auth.transport.requests
- google.oauth2.credentials
- google_auth_oauthlib
- matplotlib.pyplot
- numpy
- os
- pandas
- scipy.optimize


## References
- [Google Sheets API Docs](https://developers.google.com/workspace/sheets/api/guides/concepts)
- [Markdown Guide's cheatsheet](https://www.markdownguide.org/cheat-sheet/)
- [Choose a License](https://choosealicense.com/)
- [Pandas API Reference](https://pandas.pydata.org/pandas-docs/stable/reference/)
- [Python 3.14.6 Documentation](https://docs.python.org/3/)
- [SciPy API Reference](https://docs.scipy.org/doc/scipy/reference/)
- ...and many Stack Overflow answers of course.

