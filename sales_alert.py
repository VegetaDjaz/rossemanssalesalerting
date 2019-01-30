import csv

with open('real.csv', 'r') as real, open('predictions.csv', 'r') as pred:
    RealSales = real.readlines()
    PredictedSales = pred.readlines()

    for line in PredictedSales:
        if line in RealSales:

            outFile.write(line)




            pred = pd.read_csv(output_file)
            ##pred_columns = ['Store', 'Predicated Sales']
            real = pd.read_csv(output_file2)
            ##real_columns = ['Store', 'Real Sales']
            #new = pred.merge(real, on = ['Store'], how = 'left')
            #new[['Store', 'Predicated Sales', 'Real Sales']].to_csv(output_file3, index = False)

            for i in range(len(pred)):
                for j in range(len(real)):
            #for index, row in pred.iterrows():
            #    for index, row in real.iterrows():
                    if (pred.iloc[i:,0] == real.iloc[j:,0]):
                        temp_alert = pred.iloc[j:,1] - real.iloc[j:,1]
                        print(temp_alert)

medians = train.groupby(columns2)['Sales'].median()
medians = medians.reset_index()

test2 = pd.merge(test, medians, on = columns2, how = 'left')
assert(len(test2) == len(test))

test2.loc[test2.Open == 0, 'Store'] = 0
assert(test2.Store.isnull().sum() == 0)

test2.loc[ test2.Open == 0, 'Sales' ] = 0
assert(test2.Sales.isnull().sum() == 0)

test2[['Store', 'Sales']].to_csv(output_file, index = False)


store.loc[ store.Open.isnull(), 'Open' ] = 1
medians2 = train.groupby('Store')['Sales'].median()
medians2 = medians2.reset_index()

store2 = pd.merge(store, medians2, on = 'Store', how = 'left')
assert(len(store2) == len(store))

store2.loc[store2.Open == 0, 'Store'] = 0
assert(store2.Store.isnull().sum() == 0)

store2.loc[ store2.Open == 0, 'Sales' ] = 0
assert(store2.Sales.isnull().sum() == 0)


store2[['Store', 'Sales']].to_csv(output_file2, index = False)


#test2[[ 'Id', 'Store', 'Sales' ]].to_csv( output_file, index = False )

#medians2 = train.drop(['Date', 'Customers','DayOfWeek', 'Promo'], axis=1)
