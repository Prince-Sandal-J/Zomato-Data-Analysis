# Project: Zomato-Data-Analysis
# Author: Prince Sandal Jain
# Date: YYYY-MM-DD (you can replace with the current date)
# Description: This script analyzes Zomato data to extract insights and perform data analysis.

# Step 1 -  Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Get  CSV File from the Path
dataframe = pd.read_csv("D:\Download\Zomato data .csv")
pd.set_option('display.max_columns', None)
# print(dataframe)

#Get the complete information about the data
# dataframe.info()

#Convert datatype for the column - rate
def handlerate(value):
    value = str(value).split("/")
    value = value[0];
    return float(value)
dataframe["rate"] = dataframe["rate"].apply(handlerate)


# Question 1: What type of restaurant do the majority of customers order from?

# print(dataframe.head())

# sns.countplot(x= dataframe['listed_in(type)'],palette="Set1")
# plt.xlabel("Types of Restaurants", color ="Blue",fontsize='20')
# plt.ylabel("Count", color ="Blue",fontsize='20')
# plt.show()

# Conclusion: Majority of People order food from Dining Type Restaurant.

# Question 2: How many votes has each type of restaurant received from customers?

# print(dataframe.head())

# grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
# result = pd.DataFrame({"votes": grouped_data})
# plt.plot(result, c= "green", marker ="o")
# plt.xlabel("Types of Restaurants", color ="Red", fontsize=20)
# plt.ylabel("Votes",color = "red",fontsize=20)
# plt.show()

#  Conclusion: Dining Restaurant has maximum votes.

# Question 3: What are the ratings that the majority of restaurant has received?

# print(dataframe.head())

# plt.hist(dataframe['rate'], bins='fd', color='skyblue', edgecolor='black')
# plt.title("Ratings Distribution", fontsize=20, color="DarkBlue")
# plt.xlabel("Ratings", fontsize=15, color="Blue")
# plt.ylabel("Frequency", fontsize=15, color="Blue")
# plt.show()

# Conclusion: Majority Restaurant received ratings from 3. to 4.0

# Question 4: Zomato has observed that most couples order most of their food online. What is their average spending on each order

# print(dataframe.head())

# couple_data = dataframe['approx_cost(for two people)']
# sns.countplot(x=couple_data, palette='viridis')
# plt.xlabel("Approx Cost for couple", color="DarkBlue", fontsize=20)
# plt.ylabel("Count", color="DarkBlue", fontsize=20)
# plt.title("Distribution of Approx Cost for couple", fontsize=20, color="DarkBlue")
# plt.show()

# Conclusion: Majority couples prefer restaurants with an approx cost of Rs300

# Question 5: Which mode(Online or Offline) has received the maximum ratings?

# print(dataframe.head())

# plt.figure(figsize=(6,6))
# sns.boxplot(x='online_order',y = 'rate',data=dataframe, palette=["#3498db", "#e74c3c"])
# plt.xlabel("Online Order", color="DarkBlue", fontsize=20)
# plt.ylabel("Rating", color="DarkBlue", fontsize=20)
# plt.show()

#Conclusion: Offline Order receives lower rating in comparisn to Online Order

# Question 6: Which type of restaurants receives more offline orders, so that Zomato can provide those customers some good offers?

# print(dataframe.head())

# pivot_table = dataframe.pivot_table(index='listed_in(type)',columns='online_order',aggfunc='size',fill_value=0)
# sns.heatmap(pivot_table,annot=True,cmap='YlGnBu',fmt='d')
# plt.title("Heatmap", color="DarkBlue", fontsize=20)
# plt.xlabel("Online Order", color="DarkBlue", fontsize=20)
# plt.ylabel("Listed In(Type)", color="DarkBlue", fontsize=20)
# plt.show()

#Conclusion: Dining Restaurant primarily accept offline orders, whereas cafes primarily receive online orders. This suggest that
# clients prefer to order in person at restaurants, but prefer online ordering at cafes.