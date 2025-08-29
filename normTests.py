import matplotlib.pyplot as plt  
import seaborn as sns
from scipy import stats
import pandas as pd
import numpy as np

sns.set()

data = pd.read_csv('cleandata.csv')

# variables testing for normality
# CashbackAmount
# Tenure
# DaySinceLastOrder
# NumberOfDeviceRegistered
# Complain
# CouponUsed


#test cashBackAmount Normaility with No Churn
dataNoChurn = data[data['Churn'] == 0].copy()
dataNoChurn['CashbackAmountNorm'] = dataNoChurn['CashbackAmount'] ** 2
sns.histplot(data = dataNoChurn, x = 'CashbackAmount', bins=30)
#plt.show()
cashBackNoChurnNormTest = stats.normaltest(dataNoChurn['CashbackAmount'])
print('cashBackNoChurn NormTest pval:' + str(cashBackNoChurnNormTest.pvalue))

#test cashBackAmount Normaility with Churn
dataChurn = data[data['Churn'] == 1].copy()
dataChurn['CashbackAmountNorm'] = np.log1p(dataChurn['CashbackAmount'])
sns.histplot(data = dataChurn, x = 'CashbackAmount', bins=30)
#plt.show()
cashBackChurnNormTest = stats.normaltest(dataChurn['CashbackAmount'])
print('cashBackChurn NormTest pval:' + str(cashBackChurnNormTest.pvalue))

#tenure norm test
tenureChurnNormTest = stats.normaltest(dataChurn['Tenure'])
print('tenureChurn NormTest pval:' + str(tenureChurnNormTest.pvalue))

tenureNoChurnNormTest = stats.normaltest(dataNoChurn['Tenure'])
print('tenureNoChurn NormTest pval:' + str(tenureNoChurnNormTest.pvalue))

#DaySinceLastOrder norm test
DaySinceLastOrderChurnNormTest = stats.normaltest(dataChurn['DaySinceLastOrder'])
print('DaySinceLastOrderChurn NormTest pval:' + str(DaySinceLastOrderChurnNormTest.pvalue))

DaySinceLastOrderNoChurnNormTest = stats.normaltest(dataNoChurn['DaySinceLastOrder'])
print('DaySinceLastOrderNoChurn NormTest pval:' + str(DaySinceLastOrderNoChurnNormTest.pvalue))


#NumberOfDeviceRegistered norm test
NumberOfDeviceRegisteredChurnNormTest = stats.normaltest(dataChurn['NumberOfDeviceRegistered'])
print('NumberOfDeviceRegisteredChurn NormTest pval:' + str(NumberOfDeviceRegisteredChurnNormTest.pvalue))

NumberOfDeviceRegisteredNoChurnNormTest = stats.normaltest(dataNoChurn['NumberOfDeviceRegistered'])
print('NumberOfDeviceRegisteredNoChurn NormTest pval:' + str(NumberOfDeviceRegisteredNoChurnNormTest.pvalue))

#Complain norm test
ComplainChurnNormTest = stats.normaltest(dataChurn['Complain'])
print('ComplainChurn NormTest pval:' + str(ComplainChurnNormTest.pvalue))

ComplainNoChurnNormTest = stats.normaltest(dataNoChurn['Complain'])
print('ComplainNoChurn NormTest pval:' + str(ComplainNoChurnNormTest.pvalue))

#CouponUsed norm test
CouponUsedChurnNormTest = stats.normaltest(dataChurn['CouponUsed'])
print('CouponUsedChurn NormTest pval:' + str(CouponUsedChurnNormTest.pvalue))

CouponUsedNoChurnNormTest = stats.normaltest(dataNoChurn['CouponUsed'])
print('CouponUsedNoChurn NormTest pval:' + str(CouponUsedNoChurnNormTest.pvalue))



