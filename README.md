# California-Wine-Institute
---

# Project Description

There's a ton that goes into making a great wine (besides grapes that is) and we wanted to delve a bit deeper and get to the bottom of what makes a "great" wine versus an "okay" one. Starting with a dataset full of variables, the California Wine Institute wants us to shed a better light on the determinants of wine quality. Through feature selection, clustering, and classification modeling, we're hoping to accurately predict wine quality. 
---

# Data Dictionary

|Feature|Description|
|-|-|
|Alcohol|Percent of alcohol content|
|Citric Acid|Amount of citric acid (grams/liter)|
|Free Sulfur Dioxide|Amount of SO$_2$ (mg/L)|
|Cluster|using alcohol, citic acid, free sulfur dioxide|
|fixed_acidity|Amount of fixed acidity (grams\liter)|
|volatile_acidity|Amount of volatile acidity (grams\liter)|
|residual_sugar|Amount of residual sugar|
|chlorides|Amount of chlorides|
|total_sulfur_dioxide|amount of total sulfur dioxide| 
|density|How dense compared to water (g/mL)|
|pH|amount of pH|
|sulphates|amount of sulphates|
|wine_color|Color of wine, 0:White Wine, 1:Red Wine|
---

# Project plan
- Gather Wine Quality csvs from Data.world
- Bring files into python and join the data, seperating by color of wine
- Take initial looks and get a brief understanding of features
- Begin cleaning joined data
- Establish Initial Hypotheses 
- Explore new dataframe and perform feature selection
- Begin clustering with selected features
- Model ideal clusters and key drivers
---

# Initial assumptions
- Higher alcohol content is indicative of higher quality wine
- Clustering will play a pivotal role in improving predictive accuracy
---

# Conclusion
- 
---

# How to reproduce your work
- Create a data.world account and download both the red and white wines from "Wine Quality"
- pull data using function wrangle_wine from wine_acquire.py
- split data to train, validate, and test, stratifying on "quality" and using a random state of 117
- use kmeans to cluster data with n_clusters = 3
---
