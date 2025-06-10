import pandas as pd

#Input file name
df = pd.read_csv("")
#Column(s) that neeed to be capitialzed
df[''] = df[''].str.title()
#Delete spaces w/o data (subset for a particular column)
df = df.dropna(subset=[''])
#Delete the duplicates
df = df.drop_duplicates()
#Prints out a summary grouping the procedures and calculating the 3 values
summary = df.groupby("")[""].agg(["count", "mean", "sum"])
print(summary)
#Creates a new csv file w/o numbering
df.to_csv("cleaned_dental_data.csv", index=False)
