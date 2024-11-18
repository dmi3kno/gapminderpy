import importlib.resources
from io import StringIO
import pandas as pd

def _load_gapminder():
    content = importlib.resources('gapminder', 'gapminder.csv').decode()
    return pd.read_csv(StringIO(content))
