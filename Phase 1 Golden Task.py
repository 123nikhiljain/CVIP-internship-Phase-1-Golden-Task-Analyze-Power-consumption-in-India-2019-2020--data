#!/usr/bin/env python
# coding: utf-8

# # Phase 1 Golden Task

# # Analyze Power consumption in India(2019-2020)

# In[1]:


# Importing pandas library for data manipulation
import pandas as pd

# Importing matplotlib.pyplot for data visualization
import matplotlib.pyplot as plt

# Importing seaborn for statistical data visualization
import seaborn as sns


# In[7]:


def power_consumption_2019(df1):
    # Calculate and print total power consumption during the year 2019
    Power_consumption = df1.sum(axis=0).sort_values(ascending=False)
    print("Total power consumed during the year 2019:")
    print(Power_consumption)
    print("\n")

    # Create a DataFrame for annual consumption and plot a bar chart
    Power_consumption = df1.sum(axis=0).sort_values(ascending=False).reset_index().rename(columns={"index": "state", 0: "Annual consumption 2019"})
    state_code = ['MH', 'GJ', 'UP', 'TN', 'RJ', 'MP', 'KA', 'TG', 'AP','WB', 'PH', 'HR', 'CT','BR', 'DL', 'OR', 'KL', 'J&K', 'UK', 'HP', 'AS', 'JH', 'DNH', 'GA', 'PY', 'ML', 'TR','CH', 'MN', 'NL', 'AR', 'MZ', 'SK']
    Power_consumption.state = state_code
    plt.figure(figsize=(30, 30))
    sns.barplot(x="state", y="Annual consumption 2019", data=Power_consumption)
    plt.title("Power consumption in India during 2019")
    plt.show()

    # Calculate and print the maximum power consumed by states in a day in 2019
    max_power = df1.max(axis=0).sort_values(ascending=False)
    print("Maximum power consumed by the states in a day in 2019:")
    print(max_power)
    print("\n")

    # Calculate and print the minimum power consumed by states in a day in 2019
    min_power = df1.min(axis=0).sort_values(ascending=False)
    print("Minimum power consumed by the states in a day in 2019:")
    print(min_power)
    print("\n")


# In[8]:


def power_consumption_2020(df2):
    # Calculate and print total power consumption during the year 2020
    Power_consumption = df2.sum(axis=0).sort_values(ascending=False)
    print("Total power consumed during the year 2020:")
    print(Power_consumption)
    print("\n")

    # Create a DataFrame for annual consumption and plot a bar chart
    Power_consumption = df2.sum(axis=0).sort_values(ascending=False).reset_index().rename(columns={"index": "state", 0: "Annual consumption 2020"})
    state_code = ['MH', 'GJ', 'UP', 'TN', 'RJ', 'MP', 'KA', 'TG', 'AP', 'PH', 'HR','WB', 'DL','CT', 'BR', 'OR', 'KL', 'J&K', 'UK', 'HP', 'AS', 'JH', 'DNH', 'GA', 'PY', 'ML', 'CH', 'TR', 'MN', 'NL', 'AR', 'MZ', 'SK']
    Power_consumption.state = state_code
    plt.figure(figsize=(30, 30))
    sns.barplot(x="state", y="Annual consumption 2020", data=Power_consumption)
    plt.title("Power consumption in India during 2020")
    plt.show()

    # Calculate and print the maximum power consumed by states in a day in 2020
    max_power = df2.max(axis=0).sort_values(ascending=False)
    print("Maximum power consumed by the states in a day in 2020:")
    print(max_power)
    print("\n")

    # Calculate and print the minimum power consumed by states in a day in 2020
    min_power = df2.min(axis=0).sort_values(ascending=False)
    print("Minimum power consumed by the states in a day in 2020:")
    print(min_power)
    print("\n")


# In[9]:


def tot_power_consumption(df):
    # Calculate and print the total power consumption during 2019 and 2020
    Total_consumption = df.sum(axis=0).sort_values(ascending=False)
    print("Total power consumption during 2019 and 2020:")
    print(Total_consumption)
    print("\n")

    # Create a DataFrame for total consumption and plot a bar chart
    Total_consumption = df.sum(axis=0).sort_values(ascending=False).reset_index().rename(columns={"index": "state", 0: "Total consumption"})
    state_code = ['MH', 'GJ', 'UP', 'TN', 'RJ', 'MP', 'KA', 'TG', 'AP', 'PH', 'WB', 'HR', 'CT', 'DL', 'BR', 'OR', 'KL', 'J&K', 'UK', 'HP', 'AS', 'JH', 'DNH', 'GA', 'PY', 'ML', 'CH', 'TR', 'MN', 'NL', 'AR', 'MZ', 'SK']
    Total_consumption.state = state_code
    plt.figure(figsize=(30, 30))
    sns.barplot(x="state", y="Total consumption", data=Total_consumption)
    plt.title("Power consumption in India during 2019 and 2020")
    plt.show()


# In[ ]:


def lockdown(df3, df4):
    # Calculate total power consumption before and after the lockdown
    before = df3.sum(axis=0)
    after = df4.sum(axis=0)

    # Perform comparison and create a DataFrame
    df5 = before.compare(after)
    print(df5)

    # Plot the differences using a bar chart
    df5.plot.bar()
    plt.title("Power consumption before and after Lockdown")
    plt.show()


# In[11]:


# Read the dataset
df = pd.read_csv("dataset_tk.csv", parse_dates=True, index_col="Unnamed: 0")

# Slice the DataFrame for the year 2019
df1 = df[:359]
print("The data for the power consumed during the year 2019:")
print(df1)
print("\n")
df1.isnull().sum()

# Calculate and print power consumption for 2019
pc1 = power_consumption_2019(df1)

# Slice the DataFrame for the year 2020
df2 = df[359:]
print("The data for the power consumed during the year 2020:")
print(df2)
print("\n")
df2.isnull().sum()

# Calculate and print power consumption for 2020
pc2 = power_consumption_2020(df2)

# Print power consumption for both years
print("The power consumed during the year 2019 and 2020:")
print(df)
print("\n")
df.isnull().sum()

# Calculate and print total power consumption for both years
pc3 = tot_power_consumption(df)

# Slice the DataFrame for normal days and lockdown
df3 = df[57:146]
df4 = df[405:468]
print("The power consumed during normal days and lockdown:")
pc4 = lockdown()


# In[ ]:




