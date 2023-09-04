# How Machine Learning can help farmers select best crops

# Introduction
An integral part of assessing the soil condition is measuring the essential soil metrics such as nitrogen, phosphorous, potassium levels, and pH value. However, it can be quite an expensive and time-consuming process, which can cause farmers to prioritize which metrics to measure based on their budget constraints in order to maximize the yield of their crops

 One important factor that affects crop growth is the condition of the soil in the field, which can be assessed by measuring basic elements such as nitrogen and potassium levels. Each crop has an ideal soil condition that ensures optimal growth and maximum yield.

The dataset `soil_measures.csv`, used in this project contains:

- `"N"`: Nitrogen content ratio in the soil
- `"P"`: Phosphorous content ratio in the soil
- `"K"`: Potassium content ratio in the soil
- `"pH"` value of the soil
- `"crop"`: categorical values that contain various crops (target variable).

Each row in this dataset represents various measures of the soil in a particular field. Based on these measurements, the crop specified in the `"crop"` column is the optimal choice for that field. The dataset was prepared by `DataCamp`

In this project, We will apply machine learning to build a multi-class classification model to predict the type of `"crop"` that is suitable for that particular field.  

The model used in this project is the `multinomial Logistic Regression` because our target variable is a `multi class` variable.
