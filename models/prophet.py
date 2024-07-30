import matplotlib.pyplot as plt
from prophet import Prophet
from utils.preprocess import preprocess

if __name__ == "__main__":
    df, cap = preprocess("New Jersey")

    model = Prophet(growth='logistic')
    model.fit(df)

    future = model.make_future_dataframe(periods=365)
    future['floor'] = 0
    future['cap'] = cap

    forecast = model.predict(future)

    model.plot(forecast)
    model.plot_components(forecast)

    plt.show()
