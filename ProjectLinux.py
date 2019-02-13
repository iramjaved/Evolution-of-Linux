import pandas as pd
# Reading in the log file
git_log = pd.read_csv('Evolution of Linux/datasets/git_log.gz',compression='gzip',encoding ='latin-1', names=['timestamp','author'], header=None, sep='#')
# Printing out the first 5 rows
print(git_log.head())
print(git_log.timestamp.count())
print(git_log.author.nunique())

# Identifying the top 10 authors
git_log.groupby('author').count().sort_values('timestamp', ascending=False).head(10)

# Same as above
git_log['author'].value_counts(sort=True, ascending=False).head(10)
git_log['timestamp']= pd.to_datetime(git_log['timestamp'], unit='s')
git_log.head()
git_log['timestamp'].describe()
# determining the first real commit timestamp
first_commit_timestamp = git_log[(git_log.author=='Linus Torvalds')].timestamp.iloc[-1]
# determining the last sensible commit timestamp

last_commit_timestamp = pd.to_datetime('today')

# filtering out wrong timestamps
corrected_log = git_log[(git_log['timestamp']>=first_commit_timestamp ) & (git_log['timestamp']<=last_commit_timestamp)]


# summarizing the corrected timestamp column
corrected_log.describe()

# Counting the no. commits per year
commits_per_year = corrected_log.groupby(pd.Grouper(key='timestamp', freq='AS')).count()

# Listing the first rows

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
%matplotlib inline

fig,ax= plt.subplots()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.bar(commits_per_year.index, commits_per_year['author'], width=50, align='center')
#commits_per_year.author.plot(kind='bar',ax=ax)
plt.title('Commits made per year' )

plt.show()
