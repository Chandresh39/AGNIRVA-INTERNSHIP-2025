import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Create a dataset
data = {
    "Square_Footage": [650, 800, 1200, 1500, 2000],
    "Price": [200000, 250000, 300000, 350000, 500000]
}

# Convert to a DataFrame
df = pd.DataFrame(data)
print(df)

# Features and target
X = df[["Square_Footage"]]  # Input feature
y = df["Price"]  # Target variable

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Display model parameters
print("Intercept:", model.intercept_)  # Bias
print("Coefficient:", model.coef_)  # Weight of the feature

# Make predictions
y_pred = model.predict(X_test)

# Compare actual vs. predicted prices
print("Actual Prices:", list(y_test))
print("Predicted Prices:", list(y_pred))

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Scatter plot of data points
plt.scatter(X, y, color="blue", label="Actual Data")

# Plot regression line
plt.plot(X, model.predict(X), color="red", label="Regression Line")

plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.title("Linear Regression - House Prices")
plt.legend()
plt.show()



# new data for test model
new_data = pd.DataFrame({"Square_Footage": [1000, 1700]})
predictions = model.predict(new_data)
print("Predicted Prices for New Data:", predictions)

for sqft, price in zip(new_data['Square_Footage'], predictions):
    print(f"For {sqft} sq. feet, predicted price = ${price:,.2f}")
