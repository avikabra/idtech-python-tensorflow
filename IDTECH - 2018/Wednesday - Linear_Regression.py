import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#importing dataset code using pandas
dataset = pd.read_csv('SalaryData.csv')

#iloc is for retrieving data
X = dataset.iloc[: , :-1].values
Y = dataset.iloc[: , 1].values

#splitting to training and testing
from sklearn.cross_validation import train_test_split

#random_state is the random seed value
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

regressor = LinearRegression()
#using the two parameters to get best fit
regressor.fit(X_train, Y_train)
#best fit line values
Y_pred = regressor.predict(X_test)

print(Y_test)
print(Y_pred)

#mapping the data
plt.scatter(X_train, Y_train, color="red") #plots points
plt.scatter(X_test, Y_test, color="green")
plt.plot(X_train, regressor.predict(X_train), color="blue") #plots and connects the points
#making the graph
plt.title("Years of Experience vs. Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show();