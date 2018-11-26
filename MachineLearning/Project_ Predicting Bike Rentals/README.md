## Project
# Predicting Bike Rentals

Hadi Fanaee-T at the University of Porto compiled this Bike Rental data into a CSV file. The file contains 17380 rows, with each row representing the number of bike rentals for a single hour of a single day, which can be downloaded from the [University of California, Irvine's website](http://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset).

Here are the descriptions for the relevant columns:

- instant - A unique sequential ID number for each row
- dteday - The date of the rentals
- season - The season in which the rentals occurred
- yr - The year the rentals occurred
- mnth - The month the rentals occurred
- hr - The hour the rentals occurred
- holiday - Whether or not the day was a holiday
- weekday - The day of the week (as a number, 0 to 7)
- workingday - Whether or not the day was a working day
- weathersit - The weather (as a categorical variable)
- temp - The temperature, on a 0-1 scale
- atemp - The adjusted temperature
- hum - The humidity, on a 0-1 scale
- windspeed - The wind speed, on a 0-1 scale
- casual - The number of casual riders (people who hadn't previously signed up with the bike sharing program)
- registered - The number of registered riders (people who had already signed up)
- cnt - The total number of bike rentals (casual + registered)

In this project, I'll try to predict the total number of bikes people rented in a given hour by predicting the cnt column using all of the other columns, except for casual and registered. To accomplish this, create a few different machine learning models and evaluate their performance.


### Built with:

Python, Pandas, Numpy, matplotlib, seaborn, sklearn, LinearRegression, DecisionTreeRegressor, RandomForestRegressor, mean_squared_error, and Anaconda Jupyter Notebook.


### Project Guidelines Source:

 Path - Dataquest Data Scientist\
 Module - Machine Learning\
 Course - Decision Tree


