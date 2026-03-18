from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "Automobile.csv"

df = pd.read_csv(DATA_PATH)


def get_highest_horsepower_cars(n=5):
    '''returns the top n rows sorted by horsepower in descending order'''
    return df.sort_values("horsepower", ascending=False).head(n) 


def get_most_fuel_efficient_cars(n=5):
    '''returns the top n rows sorted by miles per gallon (mpg) in 
    descending order because higher mpg means lower fuel consumption'''
    return df.sort_values("mpg", ascending=False).head(n) 



def get_origin_statistics(): 
    '''returns summary statistics about the cars grouped by their origin, 
    including the count of cars, average miles per gallon (mpg), average horsepower, 
    and average weight for each origin category'''
    return df.groupby("origin").agg({
        "name": "count",
        "mpg": "mean",
        "horsepower": "mean",
        "weight": "mean"
    }).rename(columns={"name": "number_of_cars"})