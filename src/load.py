import pandas as pd
from sqlalchemy import create_engine

def load_dataframe_to_postgres(df: pd.DataFrame):