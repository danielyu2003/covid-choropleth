import pandas as pd
import plotly.express as px
from prophet import Prophet
from utils.states import names
from utils.preprocess import preprocess

if __name__ == "__main__":
    data = []
    for state in names:
        df, cap = preprocess(state)
        model = Prophet(growth='logistic')
        model.fit(df)
        future = model.make_future_dataframe(periods=365)
        future['floor'] = 0
        future['cap'] = cap
        forecast = model.predict(future)
        forecast['state'] = names[state]
        data.append(forecast)

    df = pd.concat(data)

    fig = px.choropleth(
        data_frame=df,
        locations='state',
        locationmode='USA-states',
        animation_frame='ds',
        color='yhat',
        color_continuous_scale='blues',
        scope='usa',
        range_color=[0, 40000]
    )

    fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 30
    fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5

    fig.show()