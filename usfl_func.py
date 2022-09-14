import pandas as pd
import plotly.express as px
from copy import copy
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go

def normalize(df):
    x = df.copy()
    for i in x.columns[1:]:
        x[i] = x[i]/x[i][0]
    return x

# We will create a function that takes in the stock prices along with the weights and retun:
# (1) Daily value of each individual securuty in $ over the specified time period
# (2) Overall daily worth of the entire portfolio 
# (3) Daily return 

def portfolio_allocation(df, weights):
    df_portfolio = df.copy()
    
    # Normalize the stock avalues 
    df_portfolio = normalize(df_portfolio)
    
    for counter, stock in enumerate(df_portfolio.columns[1:]):
        df_portfolio[stock] = df_portfolio[stock] * weights[counter]
        df_portfolio[stock] = df_portfolio[stock] * 50000
        
    df_portfolio['portfolio daily worth in $'] = df_portfolio[df_portfolio != 'Date'].sum(axis = 1)
    df_portfolio['portfolio daily % return'] = 0.0000
    
    for i in range(1, len(df)):
        # Calculate the percentage of change from the previous day
        df_portfolio['portfolio daily % return'][i] = ( (df_portfolio['portfolio daily worth in $'][i] - df_portfolio['portfolio daily worth in $'][i-1]) / df_portfolio['portfolio daily worth in $'][i-1]) * 100 
        
    # set the value of first row to zero, as previous value is not available
    df_portfolio['portfolio daily % return'][0] = 0
    
    return df_portfolio

def daily_return(df):
    df_daily_return = df.copy()
    # Loop through each stock (while ignoring time columns with index 0)
    for i in df.columns[1:]:
        # Loop through each day of a stock
        for j in range(1, len(df)):
            # Calculate the percentage of change from the previous day
            df_daily_return[i][j] = ((df[i][j]- df[i][j-1])/df[i][j-1]) * 100
            
        # set the value of first row to zero since the previous value is not available
        df_daily_return[i][0] = 0
        
    return df_daily_return

def portfolio_statistical_analysis(df, weights):
    # Get the portfolio allocation for the specified weights (sent as arguments)
    df_portfolio = portfolio_allocation(df, weights)
    
    # Cummulative return of the portfolio (Note that we now look for the last net worth of the portfolio compared to it's start value)
    cummulative_return = ((df_portfolio['portfolio daily worth in $'][-1:] - df_portfolio['portfolio daily worth in $'][0])/ df_portfolio['portfolio daily worth in $'][0]) * 100
    
    # Daily change of every stock in the portfolio (Note that we dropped the date, portfolio daily worth and daily % returns) 
    df_portfolio_daily_return = df_portfolio.drop(columns = ['Date', 'portfolio daily worth in $', 'portfolio daily % return'])
    df_portfolio_daily_return = df_portfolio_daily_return.pct_change(1) 
    
    # Portfolio Expected Annual Return 
    expected_portfolio_return = np.sum(df_portfolio_daily_return.mean() * weights * 252)
    
    # Portfolio Expected Volatility
    covariance = df_portfolio_daily_return.cov() * 252 
    expected_volatility = np.sqrt(np.dot(weights.T, np.dot(covariance, weights)))
    
    # Portfolio sharpe ratio
    sharpe_ratio = expected_portfolio_return/expected_volatility 
    
    return cummulative_return.values[0], expected_portfolio_return, expected_volatility, sharpe_ratio

from scipy.optimize import minimize

# Since optimization works as a minimizing function, we take negative of sharpe ratio and then try minimize it.

# Define a function that calculates the negative Sharpe ratio
def calculate_negative_sharpe_func(weights, df):
    cum_return, exp_portfolio_return, volatility, sharpe_ratio = portfolio_statistical_analysis(stocks_df, weights)
    return sharpe_ratio * -1

# Function to define optimization constraints (make sure sum of all weights add to 1)
def optimization_constraints_func(weights, df):
    return np.sum(weights) - 1

# Function to obtain the "volatility" for a given set of portfolio weights
def calculate_volatility_func(weights, df):
    cum_return, exp_portfolio_return, volatility, sharpe_ratio = portfolio_statistical_analysis(stocks_df, weights)
    return volatility

# Function to get the return for a particular weight
def calculate_return_func(weights, df):
    cum_return, exp_portfolio_return, volatility, sharpe_ratio = portfolio_statistical_analysis(stocks_df, weights)
    return exp_portfolio_return


def portfolio_optimization_evaluate(initialization, df, bounds, contraints_func = optimization_constraints_func, func = calculate_negative_sharpe_func):
    cummulative_return_i, portfolio_return_value_i, vol_value_i, sharpe_ratio_i = portfolio_statistical_analysis(stocks_df, initialization)
    optimization_constraint = ({'type':'eq','fun': optimization_constraints_func})
    optimization_results = minimize(func, initialization, method = 'SLSQP', bounds = bounds, constraints = optimization_constraint)
    optimized_weights = optimization_results.x
    cummulative_return_SLSQP, portfolio_return_value_SLSQP, vol_value_SLSQP, sharpe_ratio_SLSQP = portfolio_statistical_analysis(stocks_df, optimized_weights)
    return_improved = (cummulative_return_SLSQP - cummulative_return_i)/cummulative_return_i*100
    sharpe_ratio_improved = (sharpe_ratio_SLSQP - sharpe_ratio_i)/sharpe_ratio_i*100
    return return_improved, sharpe_ratio_improved
    
    