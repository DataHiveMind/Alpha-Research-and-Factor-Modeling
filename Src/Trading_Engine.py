class TradingEngine(Object):
    def __init__(self, data, model):
        self.data = data
        self.model = model
        self.signals = None

    # Download historical data for desired ticker symbol
    def download_data(self, ticker, start_date, end_date):
        data = yf.download(ticker, start=start_date, end=end_date)
        return data

    def generate_signals(self):
        self.signals = self.model.predict(self.data)
        return self.signals

    def train_model(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def evaluate_model(self, y_test, y_pred):
        mse = mean_squared_error(y_test, y_pred)
        print(f'Mean Squared Error: {mse}')
        # Add more evaluation metrics as needed