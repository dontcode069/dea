import pandas as pd

df = pd.read_csv("phones.csv")

df = df.set_index("model")

print(df)
print(len(df))