import matplotlib.pyplot as plt  
from scipy import stats
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('cleandata.csv')

# Lets take a look at the correlation matrix of the numeric values
#print(data.drop(columns=['PreferredLoginDevice','PreferredPaymentMode','Gender','PreferedOrderCat','MaritalStatus'], axis=1).corr())
# From this we can see that Tenure, NumberOfDeviceRegistered, Complain, DaySinceLastOrder, and CashbackAmount
# have the highest correlation (of the numerical data) to Churn and will likely be the most useful in modelling

#print(pd.get_dummies(data.filter(['Churn','PreferredLoginDevice','PreferredPaymentMode','Gender','PreferedOrderCat','MaritalStatus'], axis=1), drop_first=False).corr())
# From this we can see that PreferedOrderCat and MaritalStatus has a highest correlation to Churn


#CashbackAmount - ttest
#Tenure - MannWhittney U test
#DaySinceLastOrder - MannWhittney U test
#NumberOfDeviceRegistered - MannWhittney U test
#Complain - MannWhittney U test
#MaritalStatus - chi squared test
#PreferedOrderCat - chi squared test 
#CouponUsed - chi squared test 


dataNoChurn = data[data['Churn'] == 0].copy()
dataChurn = data[data['Churn'] == 1].copy()


CashbackAmountTest = stats.ttest_ind(dataChurn['CashbackAmount'], dataNoChurn['CashbackAmount'])
CashbackAmountTestPval = CashbackAmountTest.pvalue
print('T-test P-Value: ' + str(CashbackAmountTestPval))
#CashbackAmountTest T-test P-Value: 9.256833873266162e-15



TenureUTest = stats.mannwhitneyu(dataChurn['Tenure'].dropna(), dataNoChurn['Tenure'].dropna(), alternative='two-sided')
print('Tenure Mann-Whitney U Test P-Value: ' + str(TenureUTest.pvalue))
#Tenure Mann-Whitney U Test P-Value: 4.874237805370374e-158



DaySinceLastOrderUTest = stats.mannwhitneyu(dataChurn['DaySinceLastOrder'].dropna(), dataNoChurn['DaySinceLastOrder'].dropna(), alternative='two-sided')
print('DaySinceLastOrder Mann-Whitney U Test P-Value: ' + str(DaySinceLastOrderUTest.pvalue))
#DaySinceLastOrder Mann-Whitney U Test P-Value: 7.211905979665093e-31



NumberOfDeviceRegisteredUTest= stats.mannwhitneyu(dataChurn['NumberOfDeviceRegistered'], dataNoChurn['NumberOfDeviceRegistered'], alternative='two-sided')
print('NumberOfDeviceRegisteredUTest Mann-Whitney U Test P-Value: ' + str(NumberOfDeviceRegisteredUTest.pvalue))
#NumberOfDeviceRegistered Mann-Whitney U Test P-Value: 1.9038413028069075e-15



ComplainUTest= stats.mannwhitneyu(dataChurn['Complain'], dataNoChurn['Complain'], alternative='two-sided')
ComplainUTestPval = ComplainUTest
print('Complain Mann-Whitney U Test P-Value: ' + str(ComplainUTest.pvalue))
#Complain Mann-Whitney U Test P-Value: 4.274168605192964e-60



conTable = pd.crosstab(data['MaritalStatus'],data['Churn'])
MaritalStatusChiPVal = stats.chi2_contingency(conTable).pvalue
print('MaritalStatus Chi-Square Test P-Value: ' + str(MaritalStatusChiPVal))
#MaritalStatus P-Value: 2.663165164366318e-30

conTable = pd.crosstab(data['PreferedOrderCat'],data['Churn'])
PreferedOrderCatChiPVal = stats.chi2_contingency(conTable).pvalue
print('PreferedOrderCat Chi-Square Test P-Value: ' + str(PreferedOrderCatChiPVal))
#PreferedOrderCat P-Value: 1.471323314063993e-44

conTable2 = pd.crosstab(data['CouponUsed'],data['Churn'])
CouponUsedChiPVal = stats.chi2_contingency(conTable2).pvalue
print('CouponUsed Chi-Square Test P-Value: ' + str(CouponUsedChiPVal))
#print(conTable2)
#CouponUsed Chi-Square Test P-Value: 0.8473180245696922

'''
T-test P-Value: 9.256833873266162e-15
Tenure Mann-Whitney U Test P-Value: 4.874237805370374e-158
DaySinceLastOrder Mann-Whitney U Test P-Value: 7.211905979665093e-31
NumberOfDeviceRegisteredUTest Mann-Whitney U Test P-Value: 1.9038413028069075e-15
Complain Mann-Whitney U Test P-Value: 4.274168605192964e-60
MaritalStatus Chi-Square Test P-Value: 2.663165164366318e-30
PreferedOrderCat Chi-Square Test P-Value: 1.471323314063993e-44
CouponUsed Chi-Square Test P-Value: 0.8473180245696922
'''

#From this we know Tenure, NumberOfDeviceRegistered, Complain, DaySinceLastOrder, CashbackAmount, MaritalStatus, PreferedOrderCat are statistically siginifcant for determining churn