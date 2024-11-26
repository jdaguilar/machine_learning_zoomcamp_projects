# Uber Fare Prediction

## **Overview**

The main goal of this project is to develop a predictive model for Uber to estimate fare prices for their rides based on historical data.

Uber provides you a dataset of trips with complementary information like Fare, Location, Time, and Passenger Count.

This repo includes:

1. Exploratory data analysis (EDA) to understand relationships between Fare and other dataset variables.
2. The build of the regression model, including steps to clean data and select features.

## **How to Run the Project**

1. **Train the Model**:
   - First, run the `train.py` script to train the regression model. This will process the dataset and save the trained model to the specified path.
   ```bash
   python train.py
   ```

2. **Deploy the Flask App**:
   - After training the model, you can deploy the Flask application. Make sure you have the necessary dependencies installed (as specified in the `Pipfile`).
   - Run the following command to start the Flask app:
   ```bash
   pipenv run python app/app.py
   ```

3. **Access the Application**:
   - Open your web browser and navigate to `http://localhost:5000` to access the Uber Fare Prediction application.

Let me know if you need further clarifications!
[Dataset Link](https://www.kaggle.com/datasets/yasserh/uber-fares-dataset?resource=download)

