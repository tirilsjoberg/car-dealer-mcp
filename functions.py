import pandas as pd

df = pd.read_csv("Automobile.csv")


def get_top_horsepower(n=5):
    return df.sort_values("horsepower", ascending=False).head(n)


def get_best_mpg(n=5):
    return df.sort_values("mpg", ascending=False).head(n)


def get_origin_stats():
    return df["origin"].value_counts()


print("Bilene med mest hestekrefter:")
print(get_top_horsepower()[["name", "horsepower", "origin"]])

print("\nBilene med best mpg:")
print(get_best_mpg()[["name", "mpg", "origin"]])

print("\nAntall biler per opprinnelse:")
print(get_origin_stats())