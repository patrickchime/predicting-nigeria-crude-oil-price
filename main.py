# import packages
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import pickle  # to load a saved model

# Read in dataset
price = pd.read_csv("crude_oil_price.csv", index_col=0, header=0, parse_dates=['Date'])
price = price.squeeze()


app_mode = st.sidebar.selectbox('Select Page', ['Home', 'Exploration', 'Prediction'])  # three pages

if app_mode == 'Home':
    st.title('FORECASTING NIGERIAN CRUDE OIL PRICE')
    st.image('oil.jpg')
    st.write("""The time series model used to model Nigerian daily crude oil price is the
            Autoregressive Integrated Moving Average (**ARIMA**) model. The data used consists of Nigerian daily
            crude oil price from 2009 t0 2023 and this was gotten from the [Central Bank of Nigeria data portal]
            (https://www.cbn.gov.ng/rates/dailycrude.asp)""")
    st.subheader('Dataset:')
    st.write(price.head())

elif app_mode == "Exploration":
    st.subheader("Exploratory Data Analysis")

    # Build a histogram chart
    st.markdown("Histogram chart")
    num_bins = st.slider('Pick a bin', min_value=30, max_value=50, step=10)
    fig = px.histogram(price, nbins=num_bins, title="Distribution of Crude oil Price")
    fig.update_xaxes(title_text="Price [USD]")
    fig.update_yaxes(title_text="Frequency")
    st.plotly_chart(fig)

    # Build a line chart
    st.markdown("Line Chart")
    fig = px.line(price, title="Daily Crude Oil Price")
    fig.update_xaxes(title_text='Date')
    fig.update_yaxes(title_text='Crude Oil Price')
    st.plotly_chart(fig)

else:
    st.subheader("Daily Crude Oil Prediction")

    @st.cache_data
    def prediction(data):

        # split data
        cut_off = int(len(price) *0.9) # series data is split chronologically in a horizontal manner
        y_train = price.iloc[:cut_off]
        y_test =  price.iloc[cut_off:]

        # Walk-forward validation
        history = list(y_train)
        predictions = []
        
        for i in range(len(y_test)):
            
            # Fit the ARIMA model on the history data
            model = ARIMA(history, order=(1,1,0))  # ARIMA(p, d, q) order
            result = model.fit()
    
    
            # Make a one-step forecast
            output = result.forecast()  # Access the first value of the forecast tuple
    
            # Append predicted value
            predictions.append(output[0])
    
            # Update training data
            actual_test_value = y_test[i]
            history.append(actual_test_value)

            return result
        


    # call the function
    arima_model = prediction(price)

    # Get the date input from the user
    date = st.date_input("Enter the date you want to get the price prediction for")
    
    # Calculate the difference between the entered date and the last date in the time series data
    last_date = price.index[-1].date()  # Get the last date from the time series data
    date_difference = (date - last_date).days  # Calculate the difference in days



    st.markdown(f'The predicted upper and lower boundary prices of Nigerian crude oil for "{date}" is shown below: ')

    # forecasting
    forecast = arima_model.get_forecast(steps = date_difference)
    
    # get the summary of the forecasted data
    forecast_df = forecast.summary_frame()


    @st.cache_data
    def prediction_formatted(forecast):

         #build dataframe of forecast values
        forecast_df.index = pd.date_range(start=price.index[-1],
                                  periods=date_difference+1)[1:] # starts from the next day after last day in the dataset 

        # rename the index
        forecast.index.rename("Date", inplace=True)

        forecast.rename(columns = {"mean_ci_lower":"lower_boundary_price [USD]",
                                    "mean_ci_upper": "upper_boundary_price [USD]"}, inplace=True)
        
        prediction = forecast[["lower_boundary_price [USD]",
                               "upper_boundary_price [USD]"]].round(2).tail(1)
        return prediction.to_dict(orient="records")
    
    st.write(prediction_formatted(forecast_df))
        