# CS 513 - HW2
# Hogan Lin
# hlin31@stevens.edu

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------- 1. Load data ----------
filename = "./breast-cancer-wisconsin.csv"
df = pd.read_csv(filename, na_values=['?'])

print("First 5 rows:")
print(df.head())

# ---------- I. Summarize each column ----------
print("\nSummary Statistics:")
print(df.describe(include='all'))

print("\nMin/Max/Mean for numeric columns:")
print(df.describe().loc[['min', 'max', 'mean']])

# ---------- II. Identify missing values ----------
print("\nMissing values per column:")
print(df.isnull().sum())

# ---------- III. Replace missing with mean ----------
dfImputed = df.copy()
for col in dfImputed.columns:
    if dfImputed[col].dtype in [np.int64, np.float64]:
        meanVal = dfImputed[col].mean()
        dfImputed[col] = dfImputed[col].fillna(round(meanVal))

print("\nMissing values after imputation:")
print(dfImputed.isnull().sum())

# ---------- IV. Frequency table of Class vs. F6 ----------
print("\nFrequency Table (Class vs. F6):")
freqTable = pd.crosstab(dfImputed['Class'], dfImputed['F6'])
print(freqTable)

# ---------- V. Scatter plots F1 to F6 ----------
sns.pairplot(dfImputed[['F1','F2','F3','F4','F5','F6']], diag_kind="kde")
plt.suptitle("Scatter plots F1-F6", y=1.02)
plt.show()

# ---------- VI. Histogram and Boxplot for F7 to F9 ----------
subset = dfImputed[['F7','F8','F9']]

subset.hist(grid=False, bins=10, edgecolor="black", figsize=(10,4))
plt.suptitle("Histograms F7-F9")
plt.show()

subset.plot(kind="box", subplots=True, layout=(1,3), figsize=(12,4), sharey=False)
plt.suptitle("Boxplots F7-F9")
plt.show()


# ---------- 2. Reload dataset & drop rows with missing ----------
dfClean = pd.read_csv(filename, na_values=['?'])

print("\nShape before dropping missing:", dfClean.shape)
print("Missing counts before dropping:")
print(dfClean.isnull().sum())

dfClean.dropna(inplace=True)

print("\nShape after dropping missing:", dfClean.shape)
print("Missing counts after dropping:")
print(dfClean.isnull().sum())
