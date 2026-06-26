*You were the shadow of my light*  
**ALAN WALKER - FADED**

# Overview
A machine learning script to predict the time at which Alan Walker's Faded would hit four billion views on YouTube. NO AI SLOP :D

Why did I made this?
- FADED'S GONNA HIT A WHOLE FOUR BILLION VIEWS SOON AND I WANT TO PREDICT WHEN IT IS, SO THAT I CAN CELEBRATE! THAT'S ALL.

# How it works
## Recording Views
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
<dd>time elapsed since June 10, 2026 18:00. Deprecated.</dd>
</dl>
All times are in KST(UTC+9).

## Fetching Data
Using the Google Sheets API, fetch.py fetches the current sheet and stores the D/H/M/views columns in .csv format. The code is heavily based on the example in [Google Sheets API Docs](https://developers.google.com/workspace/sheets/api/guides/concepts).

## Regress!
Using scipy, main.py ~~performs~~ will perform a multivariable regression with the following model:
> a<sub>1</sub>sin(a<sub>2</sub>x + b<sub>1</sub>) + a<sub>3</sub>sin(a<sub>4</sub>x + b<sub>2</sub>) + a<sub>5</sub>exp(a<sub>6</sub>x) + a<sub>7</sub>x<sup>2</sup> + a<sub>8</sub> + b<sub>3</sub>

The two sins account for the periodic fluctuation related to the time of the day/week. Exponential accounts for the gradual increase in popularity due to *Faded*'s views getting closer to 4 billion. Added x<sup>2</sup> because it works similar to the exponential. x accounts for the constant baseline rate. And the bias exists too.

## Visualizing Results
Will use matplotllib. To be added.

## CLI
Yes, it has a CLI! To be added.

# Dependencies
- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib
- scipy


# References
- [Google Sheets API Docs](https://developers.google.com/workspace/sheets/api/guides/concepts)
- [Markdown Guide's cheatsheet](https://www.markdownguide.org/cheat-sheet/)
- [Choose a License](https://choosealicense.com/)
- [Pandas API Reference](https://pandas.pydata.org/pandas-docs/stable/reference/)
- ...and many Stack Overflow answers of course.

