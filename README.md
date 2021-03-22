# Electricity_forecasting
 This is a project to predict the capacity of backup transfer in the next week
 
 This project uses LSTM as the predictive model.  
 We use two years of operation reserve data as input to predict one week of data.

## Data pre-processing ##

When using matplotlib to plot the data to find patterns, I found that the data unit for April 2019 is different from the data units for other months. So I use pandas to solve this problem.

![before_modify](https://github.com/anfong-query/Electricity_forecasting/blob/main/plot/before_modify.png)

before modify

![after_modify](https://github.com/anfong-query/Electricity_forecasting/blob/main/plot/after_modify.png)

after modify

## correlation between operation reserve and other featue ##
Using the correlation suite of pandas, it was learned that the power plant(col = 34) most related to the operation reserve has only a 67% correlation. After testing, we decided not to use the most input feature of this power plant.

![features_correlation](https://github.com/anfong-query/Electricity_forecasting/blob/main/plot/features_correlation.PNG)

## Run the Code ##
 Create the enviroment with conda and python3.7
 ```
 conda create -n dsai python=3.7
 ```
 ```
 activate dsai
 ```
 Obtain the corresponding environment from requirement.txt
 ```
 conda install --yes --file requirements.txt
 ```
 Use the following command to predict the operation reserve for the next week
 ```
 python app.py --training data --output submission.csv
 ```
