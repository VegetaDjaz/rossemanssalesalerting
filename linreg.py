#from IPython.display import HTML, display

import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.sandbox.regression.predstd import wls_prediction_std

#import matplotlib.pyplot as plt
#import seaborn as sns
#%matplotlib inline
#sns.set_style("darkgrid")

import pandas as pd
import numpy as np

train_file = './input/train.csv'
test_file = './input/test.csv'
store_file = './input/store.csv'
output_file = 'predictions.csv'
output_file2 = 'real.csv'
output_file3 = 'final.csv'

train = pd.read_csv(train_file)
test = pd.read_csv(test_file)
store = pd.read_csv(store_file)

# merge dataframes into single dataframe by date
columns = ['Store', 'DayOfWeek', 'Date', 'Open', 'Promo', 'StateHoliday', 'SchoolHoliday']


df = (train.merge(test, on='Store')
            .merge(store, on='Store'))
