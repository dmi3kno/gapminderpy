from importlib import resources
from io import StringIO
import pandas as pd

def _load_gapminder():
    with resources.files('gapminder').joinpath('gapminder.csv').open('r', encoding='utf-8') as f:
        return pd.read_csv(f)
