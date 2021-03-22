# Electricity_forecasting
 This is a project to predict the capacity of backup transfer in the next week

## Data pre-processing ##

When using matplotlib to plot the data to find patterns, I found that the data unit for April 2019 is different from the data units for other months. So I use pandas to solve this problem.

![before_modify](https://github.com/anfong-query/Electricity_forecasting/blob/main/plot/before_modify.png)

before modify

![after_modify](https://github.com/anfong-query/Electricity_forecasting/blob/main/plot/after_modify.png)

after modify

## correlation between operation reserve and other featue ##
![features_correlation](https://github.com/anfong-query/Electricity_forecasting/blob/main/plot/features_correlation.PNG)

## Run the Code ##
 Create the enviroment with conda and python3.7
 ```
 conda create -n dsai python==3.7
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
