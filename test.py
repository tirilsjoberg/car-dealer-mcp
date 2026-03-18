import pandas as pd

df = pd.read_csv("Automobile.csv")

print("Kolonner:")
print(df.columns.tolist())

print("\nFørste 5 rader:")
print(df.head())