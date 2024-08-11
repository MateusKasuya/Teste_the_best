import pandas as pd
from src.extract import extract_csv_to_dataframe
from src.transform import transform_dataframe

main = extract_csv_to_dataframe('data/produtos 2(in).csv')

df = transform_dataframe(main)

print(df.info())

