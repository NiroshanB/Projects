import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def numtesting(data):
    #print(data.isna().sum())
    ndata = data.drop(columns=['PreferredLoginDevice', 'PreferredPaymentMode', 'Gender','PreferedOrderCat', 'MaritalStatus'], axis=1)

    # outliers
    for i in ndata:
        plt.boxplot(ndata[i].dropna(), notch=True, vert=False)
        plt.title(i)
        #plt.show()

    # The following variable appear to have a few significant outliers
    #print(data[data['Tenure'] > 40])
    #print(data[data['WarehouseToHome'] > 70])
    #print(data[data['DaySinceLastOrder'] > 20])
    #print(data[data['NumberOfAddress'] > 15])


    # Note 7 data points are missing data (approx 300 rows each)
    # Data is missing from Tenure, WarehouseToHome, HourSpendOnApp, OrderAmountHikeFromlastYear, CouponUsed, OrderCount, DaySinceLastOrder
    d = {'min': data.min(),'max': data.max()}
    ranges = pd.DataFrame(d)
    #print(ranges)


    missing = ['Tenure', 'WarehouseToHome', 'HourSpendOnApp', 'OrderAmountHikeFromlastYear', 'CouponUsed', 'OrderCount', 'DaySinceLastOrder']
    
    for i in missing:
        print(data[i].value_counts())
    

    fig, axs = plt.subplots(4, 2)
    axs[0, 0].hist(data['Tenure'])
    axs[1, 0].hist(data['WarehouseToHome'])
    axs[2, 0].hist(data['HourSpendOnApp'])
    axs[3, 0].hist(data['OrderAmountHikeFromlastYear'])
    axs[0, 1].hist(data['CouponUsed'])
    axs[1, 1].hist(data['OrderCount'])
    axs[2, 1].hist(data['DaySinceLastOrder'])
    #plt.show()


    corrdata = data.filter(['Churn']+missing, axis=1).dropna()
    print(corrdata.corr())

    # Results:
    # Tenure is right skewed, 4 extreme outliers
    # WarehouseToHome is heavily right skewed, 2 extreme outliers
    # HourSpendOnApp looks approximately normal
    # OrderAmountHikeFromlastYear is right skewed 
    # CouponUsed is heavily right skewed
    # OrderCount is heavily right skewed
    # DaySinceLastOrder is heavily right skewed, 3 possibly extreme outliers
    pass

def cattesting(data):
    # categorical variables are 'PreferredLoginDevice', 'PreferredPaymentMode', 'Gender','PreferedOrderCat', 'MaritalStatus'
    cat = ['PreferredLoginDevice', 'PreferredPaymentMode', 'Gender','PreferedOrderCat', 'MaritalStatus']
    for i in cat:
        print(i, ': ',data[i].unique())
    
    # The number of categories is relatively small indicating one-hot encoding can be used with little consequence
    # PreferredLoginDevice has 3 catergories
    # PreferredPaymentMode has 7 catergories
    # Gender has 2 catergories
    # PreferedOrderCat has 6 categories
    # MaritalStatus has 3 catergories
    # total of 21 (-5 if drop_first is used) columns if one-hot encoded
    pass

def main():
    data = pd.read_csv('E-Commerce Churn Data.csv')
    print(data.info())
    print(data.nunique())
    # functions to look st various aspect of our data
    numtesting(data)
    #cattesting(data)



    # visual inspection of this data we'll drop the few outliers that look too extreme and will likely not help with analysis
    # to avoid removing data we keep the nan values for now
    data=data[((data['Tenure'].isna())|(data['Tenure'] < 40))==True]
    data=data[((data['WarehouseToHome'].isna())|(data['WarehouseToHome'] < 70))==True]
    data=data[((data['DaySinceLastOrder'].isna())|(data['DaySinceLastOrder'] < 20))==True]
    data=data[((data['NumberOfAddress'].isna())|(data['NumberOfAddress'] < 15))==True]

    # Customer ID is unique for every row, will be dropped as it's likely unecessary
    data = data.drop(columns='CustomerID', axis=1)


    # Impute values with the mode for columns containing >2000 (~35% of all data) of the same value 
    # additionally looking at the correlation table shows these have little correlation with churn
    data['HourSpendOnApp'] = data['HourSpendOnApp'].fillna(data['HourSpendOnApp'].mode())
    data['CouponUsed'] = data['CouponUsed'].fillna(data['CouponUsed'].mode())
    data['OrderCount'] = data['OrderCount'].fillna(data['OrderCount'].mode())
    
    # Impute values with the mean for remaining little correlation columns
    data['WarehouseToHome'] = data['WarehouseToHome'].fillna(data['WarehouseToHome'].mean())
    data['OrderAmountHikeFromlastYear'] = data['OrderAmountHikeFromlastYear'].fillna(data['OrderAmountHikeFromlastYear'].mean())

    # It's difficult justify imputing the rest, thus we'll remove the remaining NaNs
    data = data.dropna()


    # For cleaned data
    data.to_csv('cleandata.csv', index=False)





if __name__ == '__main__':
    main()