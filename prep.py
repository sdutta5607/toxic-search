import pandas as pd

df = pd.read_csv("yelp.csv")

print(df['text'])

df2 = df['text']

df2.to_csv("new.csv")

df3 = pd.read_csv("new.csv")

print(df3)

from sklearn.utils import shuffle

df3 = shuffle(df3)

# df3 = df3.drop('Unnamed: 0', inplace=True, axis=1)
df3.to_csv("new1.csv")
print(df3)