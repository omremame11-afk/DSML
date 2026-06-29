import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_excel('World Cup 2018 Dataset.xlsx')
print(df)
print(df["Team"])
print(df.head(0))
print(df['Match index.1'].max())
print(df['Match index.1'].min())
print(df['Match index.1'].mean())
print(df['Match index.2'].min())
print(df['Match index.2'].max())
print(df['Match index.2'].mean())
plt.plot(df['Team'],df['Previous appearances'])
plt.xticks(rotation=90,ha='center')
plt.show()
teams = df['Team']
x = np.arange(len(teams)) 
width = 0.35             
fig, ax = plt.subplots(figsize=(15, 8))
bars_2nd = ax.bar(x - width/2, df['Match index.1'], width, label='2nd Match', color='#5DADE2')
bars_3rd = ax.bar(x + width/2, df['Match index.2'], width, label='3rd Match', color='#F1948A')
ax.bar_label(bars_2nd, labels=df['Second match against'], padding=5, rotation=90, fontsize=8, color='black')
ax.bar_label(bars_3rd, labels=df['Third match against'], padding=5, rotation=90, fontsize=8, color='black')
ax.set_xlabel('Team Name', fontsize=12, fontweight='bold')
ax.set_ylabel('Match Number / Index', fontsize=12, fontweight='bold')
ax.set_title('World Cup 2018: 2nd & 3rd Match Opponents by Team', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(teams, rotation=90, fontsize=10)
ax.legend(loc='upper left')
ax.set_ylim(0, df['Match index.2'].max() + 15)
plt.tight_layout()
plt.show()
plt.hist(df['Previous appearances'], bins=10, color='skyblue',edgecolor='black')
plt.show()
subset_df=df[['Previous appearances','Previous titles','Match index.1']]
sns.heatmap(subset_df,annot=True)
plt.show()