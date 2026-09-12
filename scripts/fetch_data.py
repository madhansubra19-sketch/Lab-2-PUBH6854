# fetch_data — loads dataset from original source
import pandas as pd

url = "https://vincentarelbundock.github.io/Rdatasets/csv/survival/pbc.csv"
pbc = pd.read_csv(url)
