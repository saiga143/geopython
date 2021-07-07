# About this repository
A mini introduction to the programming basics and scientific data analysis using python. The python libraries pandas and matplotlib will be used for reading, maupulating, analyzing and plotting data. It follows an example case where we go through different steps of processing involving different functions of python, pandas and matplotlib libraries/modules.

# Exercise-1
The `pandas` and `matplotlib` folder contains the required data, produced outputs and a jupyter notebook file with the code explained in detail how the different steps are performed which include:

1. Importing the necessary modules
2. Using functions, `for` loops and conditional statements
3. Pandas dataframe operations like:
    1. Creating, reading & writing 
    2. Indexing, selecting & Assigning
    3. Grouping & sorting
    4. Datatypes & missing values
    5. Renaming & combining
4. Matplotlib.pyplot library functions like:
    1. Creating different kinds of plots
    2. Creating sub-plots
    3. Basic plot-formatting
    4. Saving the plots 

## Task for exercise-1
The goal of this exercise is to calculate and plot seasonal weather anomalies to see how temperatures have changed in different seasons over the past 100+ years. The data used for this exercise is from the Sodankyla weather station of Finland.

**The final output is to create a four-panel plot showing the seasonal temperature anomalies for winter, spring, summer, and autumn for the years 1909-2019. 

The subplot at the end looks like the below picture

![Seasonal anomaly plot](exercise-1/images/final_plot.jpeg)

## Data
The [data](exercise-1/data/2315676.txt) used for the exercise-1 is the daily temperature data of Sodankyla weather station of Northern Finland. It contains daily temperature data from January 1908 till October 2020.

As shown below, there are a total of 6 columns in the data. Here the `TAVG`, `TMAX`, `TMIN` are in degree fahranheit. 

```
STATION           STATION_NAME                                       DATE     TAVG     TMAX     TMIN      
```