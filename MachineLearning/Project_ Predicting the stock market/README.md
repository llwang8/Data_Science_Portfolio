## Project
# Predicting the Stock Market

In this project, I work with data from the S&P500 Index. The S&P500 is a stock market index. I'll be using historical data on the price of the S&P500 Index to make predictions about future prices. Predicting whether an index will go up or down will help us forecast how the stock market as a whole will perform. Since stocks tend to correlate with how well the economy as a whole is performing, it can also help us make economic forecasts.

In this mission, I work with a csv file containing index prices. Each row in the file contains a daily record of the price of the S&P500 Index from 1950 to 2015. The dataset is stored in sphist.csv.

The columns of the dataset are:
- Date -- The date of the record.
- Open -- The opening price of the day (when trading starts).
- High -- The highest trade price during the day.
- Low -- The lowest trade price during the day.
- Close -- The closing price for the day (when trading is finished).
- Volume -- The number of shares traded.
- Adj Close -- The daily closing price, adjusted retroactively to include any corporate actions. Read more here.

I'll be using this dataset to develop a predictive model. I'll train the model with data from 1950-2012, and make predictions from 2013-2015. Evaluate the result with mean_absolute_error.


### Built with:

Python, Pandas, Numpy, matplotlib, seaborn, sklearn, LinearRegression, mean_absolute_error, and Anaconda Jupyter Notebook.


### Project Guidelines Source

 Path - Dataquest Data Scientist\
 Module - Machine Learning\
 Course - Machine Learning in Python


