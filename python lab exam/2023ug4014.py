
import numpy as np
import pandas as pd

data = pd.read_csv("AQI_Data.csv") #storing the aqi_dataset in data variable using read_csv

#common questions:

# display the first 8 rows
print(data.head(8))

print("\n\n")

#display  the last 5 rows
print(data.tail(5))

print("\n\n")


# show the dtype and number of non null values in each column
print(data.info())
data['AQI'] = pd.to_numeric(data['AQI'], errors='coerce')
data['PM2.5'] = pd.to_numeric(data['PM2.5'], errors='coerce')
data['PM10'] = pd.to_numeric(data['PM10'], errors='coerce')

print("\n\n")


# # the mean AQI,max PM2.5 and min PM10 values for each city
city_aqi = data.groupby('City')['AQI'].mean()
city_pm25 = data.groupby('City')['PM2.5'].max()
city_pm10 = data.groupby('City')['PM10'].min()




aqi_pm_data = pd.DataFrame({'Mean AQI': city_aqi, 'Max PM2.5': city_pm25, 'Min PM10': city_pm10})

print(aqi_pm_data)

print("\n\n")


# using numpy,count how many rows correspond to each unique city in the dataset and display the result as a dictionary
city_counts = np.unique(data['City'], return_counts=True)
city_counts_dict = dict(zip(city_counts[0], city_counts[1]))
print(city_counts_dict)

print("\n\n")

 
 # for each row ,compute the total sum of pollutant concentrations (PM2.5,PM10,NO2,CO,O3,SO2) using numpy
pollutant_sums = np.sum(data[['PM2.5', 'PM10', 'NO2', 'CO', 'O3', 'SO2']], axis=1)
data['Total Pollutant Concentration'] = pollutant_sums
data.to_csv('pollutant.txt', index=False)