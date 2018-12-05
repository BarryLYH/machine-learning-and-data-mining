
# coding: utf-8

# In[1]:

import pandas as pd
from collections import Counter

#Task 1
# Load Churn_dataset.csv
database = pd.read_csv('/users/barry/desktop/churn_dataset.csv', encoding = "ISO-8859-1")

#Here shows the structure of the data
print(database.describe()) #General decribition
print(database.dtypes)     #The types of features
print(len(database))       #The deep of data (Number of data)
print(database.columns)    #The name of features


#print(len(database[]))
# Search for empty values by using "isnull()" function
null_check = database.isnull().any()
print(null_check)
# Search for space values
for column in database:
    none_var = database[column].apply(lambda x: str(x).isspace()).any()
    print(column, none_var)
# We find TotalCharges has space values and the number is, and we replace the value into 0
count = 0
for i in range(len(database['TotalCharges'])):
    if database['TotalCharges'][i] == ' ':
        database['TotalCharges'][i] = '0'
        count += 1
print(count)
#We found there are 11 ' ' values in "TotalCharges" column.
#The percentage is
print('The percentage is', count/(len(database)* len(database.columns)))


# In[2]:

#task 2


import numpy as np

#I first numeric the dataset
database['customerID'] = [int(s[0:4]) for s in database['customerID']]
database['gender'] = database.gender.map({'Male':1, 'Female':0})
database['Partner'] = database.Partner.map({"No":0, 'Yes':1})
database['Dependents'] = database.Dependents.map({"No":0, 'Yes':1})
database['PhoneService'] = database.PhoneService.map({"No":0, 'Yes':1})
database['MultipleLines'] = database.MultipleLines.map({"No":0, 'Yes':1, 'No phone service':-1})
database['InternetService'] = database.InternetService.map({"No":-1, 'DSL':0, 'Fiber optic':1})
database['OnlineSecurity'] = database.OnlineSecurity.map({"No":0, 'Yes':1,'No internet service':-1})
database['OnlineBackup'] = database.OnlineBackup.map({"No":0, 'Yes':1, 'No internet service':-1})
database['DeviceProtection'] = database.DeviceProtection.map({"No":0, 'Yes':1, 'No internet service':-1})
database['TechSupport'] = database.TechSupport.map({"No":0, 'Yes':1, 'No internet service':-1})
database['StreamingTV'] = database.StreamingTV.map({"No":0, 'Yes':1, 'No internet service':-1})
database['StreamingMovies'] = database.StreamingMovies.map({"No":0, 'Yes':1, 'No internet service':-1})
database['Contract'] = database.Contract.map({'Month-to-month':0, 'One year':1, 'Two year':2})
database['PaperlessBilling'] = database.PaperlessBilling.map({"No":0, 'Yes':1})
database['PaymentMethod'] = database.PaymentMethod.map({"Electronic check":0, 'Mailed check':1, 'Bank transfer (automatic)':2, 'Credit card (automatic)':3})
database.TotalCharges  = [float(i) for i in database.TotalCharges]
database['Churn'] = database.Churn.map({"No":0, 'Yes':1})

# Since I what to use pearson correlation, we should normalize the data into normal distribution
# The normalization of columns and we leverage zero-mean normalization
average = np.mean(np.array(database['TotalCharges']))
variant = np.var(np.array(database['TotalCharges']))
database.TotalCharges  = [(i-average)/variant for i in database.TotalCharges]

average = np.mean(np.array(database['MonthlyCharges']))
variant = np.var(np.array(database['MonthlyCharges']))
database.MonthlyCharges  = [(i-average)/variant for i in database.MonthlyCharges]

average = np.mean(np.array(database['tenure']))
variant = np.var(np.array(database['tenure']))
database.tenure   = [(i-average)/variant for i in database.tenure]

# here is the calculation of pearson correlations between input variables and target output Churn
corr = database.corrwith(database.Churn)
print(corr)


#Pearson correlations show the linear relation between features and target. The absolute value close to 1 means it has
#better correlation. Here, I select the features whose pearson correlations absolute values are bigger than 0.15.
# So I select SeniorCitizen, Partner, Dependents, tenure, InternetService,StreamingTV, StreamingMovies, Contract, PaperlessBilling
#PaymentMethod,MonthlyCharges,TotalCharges

# Next, I choose RandomForest model to do classification and Randomforest doesn't depend on feature selection. However, 
#from correlations we still can do a quick seleciton.


# In[5]:

#task3


# Here the machine learning model we want to use it RandomForest. The reasons are:
# 1. The dataset is not deep enough, so we cannot use deep learning method it will result in overfitting.
# 2. RandomForest has a great performance in classificiant problems and a high-level accuracy
# 3. RandomForest is based on bootstraping which supply enough randomness that can prevent overfitting
# 4. It can figure out large-scale features problem and doesn't depend on feature selection.
# 5. Good at process discrete data and our data is a typecial discrete data with lots of yes/no(1/0)
# 6. RandomForest is time-consuming when data is large, but our data is small.

features = ['SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'InternetService','StreamingTV',
            'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges']

X = database[features]
y = database['Churn']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42)

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification


RF_model = RandomForestClassifier(n_estimators=100, max_depth=15, random_state=42)
RF_model.fit(X_train, y_train)

#return the accuracy
print(RF_model.score(X_test,y_test))


# In[8]:

# RandomForest is funcy bagging machine learning algorithm. I also try another boosting algorithm "CATboosting"
# CATboosting is a machine learning algorithm which is really good at classification problem.
import catboost as cb

model = cb.CatBoostClassifier(iterations=100, depth=12, learning_rate=0.05, loss_function='Logloss',
                              logging_level='Verbose')
model.fit(X_train, y_train)

print(model.score(X_test, y_test))


# In[ ]:



