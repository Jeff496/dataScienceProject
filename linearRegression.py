# splitting data to train and test linear regression

# independent variable or number of fans at a game
# X = test.iloc[,].values
# dependent variable or chance of winning the game
# y = test.iloc[,].values

# splitting the dataset
#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test =train_test_split(X,y,test_size=1/3,random_state=0)

# fitting the regression model
# from sklearn.linear_model import LinearRegression
# regressor = LinearRegression()
# regressor.fit(X_train,y_train)

# predicting the test set results
# y_pred = regressor.predict(X_test)
# y_pred
#y_test

# visualizing the results
#plot for the TRAIN
# plt.scatter(X_train, y_train, color='red') # plotting the observation line
# plt.plot(X_train, regressor.predict(X_train), color='blue') # plotting the regression line
# plt.title("Effect of Fans on Win Percentage (Training set)") # stating the title of the graph
# plt.xlabel("Number of Fans") # adding the name of x-axis
# plt.ylabel("Chance of Winning") # adding the name of y-axis
# plt.show() # specifies end of graph
#plot for the TEST
# plt.scatter(X_test, y_test, color='red')
# plt.plot(X_train, regressor.predict(X_train), color='blue') # plotting the regression line
# plt.title("Effect of Fans on Win Percentage (Testing set)")
# plt.xlabel("Number of Fans")
# plt.ylabel("Chance of Winning")
# plt.show()