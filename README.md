# Introduction
Farmers want to know which crop would grow best in their soil. Different crops like corn, wheat, or tomatoes need different things from the soil to thrive. One important factor that affects crop growth is the condition of the soil in the field, which can be assessed by measuring basic elements such as nitrogen, phosphorus, ph and potassium levels. Each crop has an ideal soil condition that ensures optimal growth and maximum yield.

To help farmers with this important decision, we will build a model called "Crop Predictor." This model could look at the soil in farmer's field and tell him which crop would be the most suitable to plant.

The dataset `soil_measures.csv`, used in this project contains:

- `"N"`: Nitrogen content ratio in the soil
- `"P"`: Phosphorous content ratio in the soil
- `"K"`: Potassium content ratio in the soil
- `"pH"` value of the soil
- `"crop"`: categorical values that contain various crops (target variable).

Each row in this dataset represents various measures of the soil in a particular field. Based on these measurements, the crop specified in the `"crop"` column is the optimal choice for that field. The dataset was prepared by `DataCamp`

In this project, We will apply machine learning to build a multi-class classification model to predict the type of `"crop"` that is suitable for that particular field.  

The model used in this project is the `multinomial Logistic Regression` because our target variable is a `multi class` variable.
