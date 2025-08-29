import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.utils.validation import column_or_1d
import seaborn as sns




# As noted in statsTest.py and dataVisualizations.py the following appear useful for modeling
# Tenure, NumberOfDeviceRegistered, Complain, DaySinceLastOrder, CashbackAmount, MaritalStatus, PreferedOrderCat



def main():
    df = pd.read_csv('cleandata.csv')
    df = df.filter(['Churn','Tenure', 'NumberOfDeviceRegistered', 'Complain', 'DaySinceLastOrder', 'CashbackAmount', 'MaritalStatus', 'PreferedOrderCat'])
    
    # onehot encode Marital status and PreferedOrderCat using dummy variables
    dfenc = pd.get_dummies(df)
    X = dfenc.drop(['Churn'], axis=1)
    y = dfenc.filter(['Churn'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
    y_train = column_or_1d(y_train)
    y_test = column_or_1d(y_test)


    kncmodel = KNeighborsClassifier(n_neighbors=3)
    kncmodel.fit(X_train, y_train)
    print('KNeighborsClassifier: ',kncmodel.score(X_test, y_test))
    # Score: 0.8431372549019608
    # This result is quite good



    rdmodel = RandomForestClassifier(n_estimators=100)
    rdmodel.fit(X_train, y_train)
    print("RandomForestClassifier: ",rdmodel.score(X_test, y_test))
    # Score: 0.9486461251167133
    # This result is better


    gnbmodel = GaussianNB()
    gnbmodel.fit(X_train, y_train)
    print("GaussianNB: ",gnbmodel.score(X_test, y_test))
    # Score: 0.39402427637721754
    # This occurs as GaussianNB is expecting the underlying dataset to be normal (which as seen in normtests.py is not true)


    # it looks like random forest is giving use the best results lets plot the prediction vs data
    predictions = rdmodel.predict(X_test)
    pltdata = pd.DataFrame({'Predicted Churn': predictions, 'Real Churn': y_test})
    sns.set_theme(style="white")
    sns.histplot(pltdata, multiple='dodge', bins=2)
    plt.show()




if __name__ == '__main__':
    main()