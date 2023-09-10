# Predicting Nigerian Daily Crude Oil Price


## Introduction

The time series model used to model Nigerian daily crude oil price is the Autoregressive Integrated Moving Average (**ARIMA**) model. The data used consists of Nigerian daily crude oil price from 2009 t0 2023 and this was gotten from the [Central Bank of Nigeria data portal](https://www.cbn.gov.ng/rates/dailycrude.asp). The measure of accuracy of forcast used in this work is the ***mean absolute error (MAE)***.

## Conclusion

The AutoRegressive Integrated Moving Average (ARIMA) was used as a model to analyse the Nigerian daily crude oil price from october 23, 2009 to September 4, 2023. After parameter tuning (GridSearch), ARIMA(1,1,0) was chosen as the optimal model. The model was concluded as satisafactory for forecasting since the ACF and PACF of the residuals do not form any irregular pattern. The model was used to forecast Nigerian crude oil price for the next 118 days, starting from September 5, 2023 to December 31, 2023. The forecasted values of the Nigerian daily crude oil price were observed to be between  $88.58 - $131.71 by the end of the year, 2023. The evaluation metric used indicated that the forecasted values are relatively accurate.