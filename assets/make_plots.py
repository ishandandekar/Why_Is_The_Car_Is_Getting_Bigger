# Python file to make plots for README and Medium article

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plt.subplots_adjust(left=0.5,
                    bottom=0.5,
                    right=0.9,
                    top=0.9,
                    wspace=0.9,
                    hspace=0.9)

FILE_PATH = r"../us-accidents/US_Accidents_Dec21_updated.csv"
df = pd.read_csv(FILE_PATH, index_col=0)

plt.figure(figsize=(15, 10))

cities_sorted = df.City.value_counts()
plt.subplot(2, 3, 1)
cities_sorted[:20].plot(kind='barh')
plt.title("Number of accidents sorted by cities")
plt.subplot(2, 3, 2)
sns.histplot(cities_sorted, log_scale=True)
plt.title("Histogram of accidents sorted by cities")

df.Start_Time = pd.to_datetime(df.Start_Time)
plt.subplot(2, 3, 3)
plt.title("Distribution of accidents over hours of a day")
sns.distplot(df.Start_Time.dt.hour, bins=24, kde=False, norm_hist=True)

plt.subplot(2, 3, 4)
plt.title("Distirbution of accidents over a week")
sns.distplot(df.Start_Time.dt.dayofweek, bins=7, kde=False, norm_hist=True)

plt.subplot(2, 3, 5)
df_2020 = df[df['Start_Time'].dt.year == 2020]
sns.distplot(df_2020.Start_Time.dt.month, bins=12, kde=False, norm_hist=True)
plt.title("Distribution of accidents over months of year (2020)")

plt.subplot(2, 3, 6)
plt.bar(x=df.Severity.value_counts().index,
        height=df.Severity.value_counts().values)
plt.xticks(df.Severity.value_counts().index)
plt.title("Countplot of Severity of accidents")

plt.savefig('myimage.png', format='png', dpi=1200)
# plt.show()
