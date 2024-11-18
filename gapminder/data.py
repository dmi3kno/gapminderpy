from importlib import resources
from io import StringIO
import pandas as pd

def _load_gapminder():
    content = resources.path('gapminder', 'gapminder.csv').decode()
    return pd.read_csv(StringIO(content))
