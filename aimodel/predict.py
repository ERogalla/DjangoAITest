import pickle
from sklearn.externals import joblib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

sc = MinMaxScaler()
mdl = joblib.load('loan_model.pkl')
X = pd.read_excel('test.xlsx')
X_test = sc.fit_transform(X)
y_pred = mdl.predict(X_test)
y_pred = (y_pred>0.58)

val = pd.DataFrame(y_pred, columns=['Status'])
val = val.replace({True: 'Approved', False: 'Rejected'})
print(val)