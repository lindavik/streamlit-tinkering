from pycaret.datasets import get_data
from pycaret.classification import *
import pandas as pd


def start():
    diabetes: pd.DataFrame = get_data('diabetes')
    print(diabetes)
    experiment = setup(diabetes, target='Class variable')
    compare_models()


if __name__ == '__main__':
    start()