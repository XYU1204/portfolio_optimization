# portfolio_optimization
* Created a tool that estimates data science salaries (MAE ~ $ 11K) to help data scientists negotiate their income when they get a job.
* Scraped over 1000 job descriptions from glassdoor using python and selenium
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark. 
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model. 

## Code and Resources Used 
**Python Version:** 3.7  
**Packages:** pandas, numpy, scipy, sklearn, matplotlib, seaborn, plotly, os, re

## [Data Preparation](https://github.com/XYU1204/portfolio_optimization/blob/main/data_cleaning_processing.ipynb) 
In this project, we studied 5 year stocks market data of the top 10 most traded stock. The data is obtained from [https://www.kaggle.com/datasets/mdwaquarazam/stock-price-history-top-10-companies] (https://www.kaggle.com/datasets/mdwaquarazam/stock-price-history-top-10-companies). The original data has 11 csv files. Each file includes date of trading,	open price, highest price of the trading day,	lowest price of the trading day, close price,	volume of stocks, and name of the Company. We assume we trade at most once a day at open price. We extract the open price column of each csv file, and make a pandas dataframe that consists of open prices of each stock on each trading day.
![alt text](https://github.com/XYU1204/portfolio_optimization/blob/main/stocks_df.png)

## [Exploratory Data Analysis and Simple Portfolio Statistics](https://github.com/XYU1204/portfolio_optimization/blob/main/EDA_and_simple_portfolio_allocation.ipynb)
![alt text](https://github.com/XYU1204/portfolio_optimization/blob/main/all_stocks_normalized.png "Normalized stock price over time")
Normalized stock price over time (price on later date compared to price on the first day of the data set).

![alt text](https://github.com/XYU1204/portfolio_optimization/blob/main/daily_return_frequency.png "daily return distribution")
Daily return rate distribution for each stock. If the daily return is more "spread out", the stock is more volatile. According to the figure, Tesla is the most volatile stock.
