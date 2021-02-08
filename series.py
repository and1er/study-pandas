"""Explore series data object."""

import pandas as pd

if __name__ == '__main__':
    my_series = pd.Series([5, 6, 7, 8, 9, 10])
    print(f'String repr:\n{my_series}\n')
    print(f'Indexes:\n{my_series.index}\n')
    print(f'Values:\n{my_series.values}\n')
    print(f'Get value by index:\n{my_series[4]}\n')
    print(f'Get by index range:\n{my_series[2:5]}\n')
