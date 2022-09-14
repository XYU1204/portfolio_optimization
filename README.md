# portfolio_optimization
* Created a tool that estimates data science salaries (MAE ~ $ 11K) to help data scientists negotiate their income when they get a job.
* Scraped over 1000 job descriptions from glassdoor using python and selenium
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark. 
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model. 

## Code and Resources Used 
**Python Version:** 3.7  
**Packages:** pandas, numpy, scipy, sklearn, matplotlib, seaborn, plotly, os, re

## [Data Preparation](https://github.com/XYU1204/portfolio_optimization/blob/main/data_cleaning_processing.ipynb) 
In this project, we studied 5 year stocks market data of the top 10 most traded stock. The data is obtained from [kaggle](https://www.kaggle.com/datasets/mdwaquarazam/stock-price-history-top-10-companies). The original data has 11 csv files. Each file includes date of trading,	open price, highest price of the trading day,	lowest price of the trading day, close price,	volume of stocks, and name of the Company. We assume we trade at most once a day at open price. We extract the open price column of each csv file, and make a pandas dataframe that consists of open prices of each stock on each trading day.
![alt text](https://github.com/XYU1204/portfolio_optimization/blob/main/stocks_df.png)

## [Exploratory Data Analysis and Simple Portfolio Statistics](https://github.com/XYU1204/portfolio_optimization/blob/main/EDA_and_simple_portfolio_allocation.ipynb)
![alt text](https://github.com/XYU1204/portfolio_optimization/blob/main/all_stocks_normalized.png "Normalized stock price over time")

Normalized stock price over time (price on later date compared to price on the first day of the data set).


![alt text](https://github.com/XYU1204/portfolio_optimization/blob/main/daily_return_frequency.png "daily return distribution")

Daily return rate distribution for each stock. If the daily return is more "spread out", the stock is more volatile. According to the figure, Tesla is the most volatile stock.


![alt text](https://github.com/XYU1204/portfolio_optimization/blob/main/correlation_matrix.png "correlation matrix")

Correlation matrix of the 10 stocks. Visualize using seaborn. According to the correlation matrix, Walmart has small correlation in daily return with all other stocks. The reason might be that it belong to retail industry. Microsoft and Apple has the highest correlation at 0.74. They both belong to IT industry.

![alt text](https://github.com/XYU1204/portfolio_optimization/blob/main/portfolio_worth_over_time.png "Simple portfolio with equal weights")

created a simple portfolio with equal weight (invest 5000 dollar equally to each stock). The figure shows the portfolio worth over time.

**Apply CAPM formula to calculate the return for the portfolio**  

#### The CAPM formula is represented as following: ####

 $ r_i = r_f + \beta_i (r_m -r_f) $
 
 $r_i$: expected return of a security
 
 $r_f$: risk free return of the market, here we will use 0%
 
 $r_m$: expected return of the market, here we will use S & P 500
 
 $\beta_i$: beta between the stock and the market
 
For S&P 500 (which we use as $r_m$), we downloaded data from https://www.marketwatch.com/investing/index/spx/download-data. We parsed the data file and chose the same date range as the 10 stocks.

Expected return per year based on CAPM for the portfolio is 15.3%
