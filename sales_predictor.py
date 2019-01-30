#!/usr/bin/env python
import pandas as pd
from matplotlib import pyplot

train_file = './input/train.csv'
test_file = './input/test.csv'
store_file = './input/store.csv'
output_file = 'predictions.csv'
output_file2 = 'real.csv'
output_file3 = 'final.csv'

train = pd.read_csv(train_file)
test = pd.read_csv(test_file)
store = pd.read_csv(store_file)

# remove rows with zero sales
# mostly days where closed, but also 54 days when not
train = train.loc[train.Sales > 0]

# remove NaNs from Open
test.loc[ test.Open.isnull(), 'Open' ] = 1

# Group sales by stores, day of week and promo, so we will have a sales value
# for each configuration.
# i.e : For a given store on a given day, with and without promo
# We have enough data to get medians/means for every possible combination of
# these three variables.
columns = ['Store', 'DayOfWeek', 'Promo']
medians = train.groupby(columns)['Sales'].median()
medians = medians.reset_index() #converts medians from a series to a data frame.

# For now, we have the medians/means and want to produce predictions for the test set.
# Accordingly, there are two data frames, or tables: test and medians/means.
# For each row in test, we’d like to pull an appropriate median
test2 = pd.merge(test, medians, on = columns, how = 'left')
#The resulting frame should have as many rows as the original test
assert(len(test2) == len(test))

test2.loc[test2.Open == 0, 'Store'] = 0
assert(test2.Store.isnull().sum() == 0)

test2.loc[ test2.Open == 0, 'Sales' ] = 0
assert(test2.Sales.isnull().sum() == 0)

# write in a CSV the output of the predicated sales
test2[['Store', 'Sales']].to_csv(output_file, index = False)

#pyplot.scatter(test2.Store, test2.Sales)
#pyplot.show()

# create a basic reference CSV with the sales value per store to compare and create a scale
store = train.drop(['DayOfWeek','Date','Customers','Open','Promo','StateHoliday','SchoolHoliday'], axis=1)
#store = store.groupby("Store")['Sales'].median() #create a mean sales value by store whatever day of the week is it or other data may intefer
#store = store.reindex(['Store', 'Sales'])
store[['Store', 'Sales']].to_csv(output_file2)

pred = pd.read_csv(output_file)
real = pd.read_csv(output_file2)
#pred = real.groupby("Store")['Sales']
#final = (pred.merge(real, on='date')
final = pd.merge(left=pred, right=real, on = 'Store', how = 'left')
#final[['Store', 'Sales_x', 'Sales_y']].to_csv(output_file3, index = False)
print( "Done!" )
