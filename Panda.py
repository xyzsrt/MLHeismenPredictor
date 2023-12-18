# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

historical_data = pd.read_csv('PrevWinners.csv')
CurrentPlayers = pd.read_csv('CurrentPLayers.csv')

features = ['PassAtt', 'PassCom', 'PassYDS', 'PassTD']
X = historical_data[features]
y = historical_data['PassEFF']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

CurrentCanidates = model.predict(CurrentPlayers[features])

plt.scatter(X_test['PassYDS'], y_test, color='black', label='Actual Winners')
plt.scatter(X_test['PassYDS'], predictions, color='blue', label='Predicted Winners')
plt.xlabel('Passing Yards')
plt.ylabel('Winner')
plt.legend()
plt.show()

potential_winner = CurrentPlayers.loc[CurrentCanidates.argmax()]
print(f"The potential Heisman winner among current candidates is:\n{potential_winner}")
