import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Assume we have a DataFrame 'df' with columns 'feature1', 'feature2', ..., 'featureN' and 'target'
df = pd.read_csv('financial_data.csv')

# Separate features and target
features = df.drop('target', axis=1)
target = df['target']

# Split the data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)

print(f'The mean squared error of the model is {mse}')


import QuantLib as ql

# Define option parameters
spot_price = 100
strike_price = 105
expiry = 1  # 1 year
volatility = 0.2
risk_free_rate = 0.05

# Create option objects
option_type = ql.Option.Call
exercise_date = ql.Date(31, 12, 2024)
payoff = ql.PlainVanillaPayoff(option_type, strike_price)
exercise = ql.EuropeanExercise(exercise_date)

# Create Black-Scholes process
spot_handle = ql.QuoteHandle(ql.SimpleQuote(spot_price))
flat_ts = ql.YieldTermStructureHandle(ql.FlatForward(0, ql.NullCalendar(), ql.QuoteHandle(ql.SimpleQuote(risk_free_rate)), ql.Actual360()))
flat_vol_ts = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(0, ql.NullCalendar(), ql.QuoteHandle(ql.SimpleQuote(volatility)), ql.Actual360()))
bs_process = ql.BlackScholesProcess(spot_handle, flat_ts, flat_vol_ts)

# Calculate option price
european_option = ql.VanillaOption(payoff, exercise)
european_option.setPricingEngine(ql.AnalyticEuropeanEngine(bs_process))
option_price = european_option.NPV()

print(f"European Call Option Price: ${option_price:.2f}")
