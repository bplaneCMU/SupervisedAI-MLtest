import sys
import numpy as np
import pandas as pd

'''
Removes empty columns and columns with only one value
from csv, and writes to file at PATH_cleaned.csv
'''
def __main(path, export=False):
    frame = pd.read_csv(path, na_values='')
    #Drop empty columns
    frame.dropna(axis=1, how='all', inplace=True)
    #Find number of unique values in each col
    u_vals = frame.apply(pd.Series.nunique)
    #Drop all columns with only one unique value
    cols_to_drop = u_vals[u_vals == 1].index
    frame.drop(cols_to_drop, axis=1, inplace=True) 

    if export:
        frame.to_csv(path[:-4] + '_cleaned.csv', index=False)

    return frame

'''
Public clean function
'''
def clean(path, this_export=False):
    return __main(path, export=this_export)

if __name__ == '__main__':
    path = sys.argv[1]
    if path is None:
        quit()
    __main(path, export=True)