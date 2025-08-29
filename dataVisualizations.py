import matplotlib.pyplot as plt  
import seaborn as sns
import pandas as pd
import numpy as np

data = pd.read_csv('cleandata.csv')

# Lets take a look at the correlation matrix of the numeric values
#print(data.drop(columns=['PreferredLoginDevice','PreferredPaymentMode','Gender','PreferedOrderCat','MaritalStatus'], axis=1).corr())
# From this we can see that Tenure, NumberOfDeviceRegistered, Complain, DaySinceLastOrder, and CashbackAmount
# have the highest correlation (of the numerical data) to Churn and will likely be the most useful in modelling

#print(pd.get_dummies(data.filter(['Churn','PreferredLoginDevice','PreferredPaymentMode','Gender','PreferedOrderCat','MaritalStatus'], axis=1), drop_first=False).corr())
# From this we can see that PreferedOrderCat and MaritalStatus has a highest correlation to Churn

# As these are the columns we'll likely be modelling with at let's take a closer look at them to see if they're actually useful
numerical = ['Churn', 'Tenure', 'DaySinceLastOrder', 'CashbackAmount']
categorical = ['Churn', 'PreferedOrderCat', 'MaritalStatus', 'Complain', 'NumberOfDeviceRegistered']

sns.set_theme(style="ticks")
#sns.pairplot(data.filter(numerical, axis=1), hue="Churn", kind="kde")
plt.show()


sns.set_theme(style="white")
fig, axs= plt.subplots(1, 2)
sns.countplot(data=data, x="Complain", hue="Churn", ax=axs[0])
sns.countplot(data=data, x="NumberOfDeviceRegistered", hue="Churn", ax=axs[1])
fig.tight_layout()
plt.show()


sns.set_theme(style="white")
fig, axs= plt.subplots(1, 2)
sns.countplot(data=data, x="PreferedOrderCat", hue="Churn", ax=axs[0])
sns.countplot(data=data, x="MaritalStatus", hue="Churn", ax=axs[1])
axs[0].tick_params(axis='x', rotation=60)
axs[1].tick_params(axis='x', rotation=60)
fig.tight_layout()
fig.align_labels(axs)
plt.show()






