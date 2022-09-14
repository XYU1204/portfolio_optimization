# portfolio_optimization
* Prepared stock market data from various sources. Performed portfolio analysis using CAPM (capital asset pricing model).
* Portfolio Optimization using 2000 Monte Carlo Simulations.
* Optimize arbitrary initial portfolio weights by maximizing sharpe_ratio using SLSQP (Sequential Least Squares Programming). 
* On average, the optimizer increased expected annual return by 73.99%, and increase expected sharpe ratio by 25.40%, making the investment more profitable and less violatile at the same time.

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

When investing, we need to decide which percentage (weight) of our investment money goes to which stock. In simple case, we created a portfolio with equal weight (invest 5000 dollar equally to each stock). The figure shows the portfolio worth over time.


**Apply CAPM formula to calculate the return for the portfolio**  

 The CAPM formula is represented as following:

 $ r_i = r_f + \beta_i (r_m -r_f) $
 
 $r_i$: expected return of a security
 
 $r_f$: risk free return of the market, here we will use 0%
 
 $r_m$: expected return of the market, here we will use S & P 500
 
 $\beta_i$: beta between the stock and the market
 
For S&P 500 (which we use as $r_m$), we downloaded data from https://www.marketwatch.com/investing/index/spx/download-data. We parsed the data file and chose the same date range as the 10 stocks.

We used linear regression between each stock and S&P 500 to find beta. 

Expected return per year based on CAPM for the portfolio is 15.3%

## [Model Building and Portfolio Optimization](https://github.com/XYU1204/portfolio_optimization/blob/main/portfolio_optimization.ipynb)

In our usfl_fun module, we created two functions to allocate portfolio according to weights, and to calculate relevant statistics for the portfolios.

The statistics are calculated as following:

expected_annual_portfolio_return = sum(avg_daily_return_of_each_stock * weights * 252_trading_days_per_year)

expected_annual_violatility (standard deviation) = $\sqrt{w^T \Sigma w}$, where W is the weight vector, and $\Sigma$ is the covariance matrix of the daily_return_rate of stocks * 252_trading_days_per_year

sharpe_ratio = expected_annual_portfolio_return/expected_annual_volatility

We ran 2000 simulations with randomized normalized weights, calculated their relevant statistics. We found the best portfolio among the 2000 by choosing the one with the highest sharpe ratio shown as following.

![alt text](https://github.com/XYU1204/portfolio_optimization/blob/main/newplot.png "best sharpe ratio")

Now, for any given arbitrary portfolio, we can perform optimization by maximizing the sharpe ratio using Sequential Least Squares Programming. In our example, we tried an initialization of [0.04307998, 0.02908569, 0.09863662, 0.00991209, 0.04099922, 0.20746367, 0.12461258, 0.26182388, 0.04255328, 0.14183299]. The initialization has annual portfolio return of 222% and sharpe ratio of 0.913. Such portfolio profile is expected to be profitable but highly violatile, which means investors would quickly loose assest as well. After optimization, we found the optimal portfolio weights to be [2.19955699e-01, 1.41091263e-01, 6.80298803e-17, 4.45286229e-01, 3.56770535e-17, 1.93666809e-01, 3.35075580e-17, 7.89658044e-17, 2.40790986e-17, 1.75234249e-17]. The optimized portfolio has annual return of 464%, which is a 208.8% improvement compared to initialization, and sharpe ratio of 0.913, which is a 145.1% improvement comapred to initialization. The optimized portfolio is more profitable and more stable at the same time. 


## [Evaluating Optimizer]
To evaluate the performance of the optimizer we created, we randomly generated 50 initialization feed to the optimizer. We compared the percentage increase in annual return and in sharpe ratio before and after optimization. On average, our optimizer shows 73.99% increase in expected annual return, and 25.40% increase in expected sharpe ratio. 
