import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('kd-meta-analysis.csv')
sns.barplot(df, x="KD Duration (weeks)", y="Mean HbA1c Change (%)", hue="Design")
plt.title('Change in HbA1c vs Ketogenic Diet Duration')
plt.show()
