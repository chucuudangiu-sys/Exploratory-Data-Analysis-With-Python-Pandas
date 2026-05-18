""" Import Libary """

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
# set up display
pd.set_option('display.width', 1000)

# See data imported 
df = pd.read_csv('DATASET RUN.csv', low_memory=False)

# print(df.head(10))
# print(df.dtypes)
# print(df.shape)

""" Clean Up Data """

# Only want USA races, 50k - 50 mil, 2020 

# show 50k or 50 mil races 

# race_show = df[df["Event distance/length"]  ==  '50km'] 
# race_show = df[df["Event distance/length"] == '50mi']
# COMBINE 50k/50mi isin 

# race_show = df[(df["Event distance/length"].isin(['50km','50mi'])) & (df["Year of event"] == 2020)]
# print(race_show)
""" 1st data cleaning part """
df2 = (df[(df["Event name"].str.split('(').str.get(1).str.split(')').str.get(0) == "USA")
          & (df["Event distance/length"].isin(['50km','50mi']))
          & (df["Year of event"] == 2020)])  

# remove (USA) fromm event name 

df2["Event name"] = df2["Event name"].str.split('(').str.get(0)

# Clean Athelete age 

df2["Athlete age"] = 2020 - df2["Athlete year of birth"]

# Remove h from Athlete performance 

df2["Athlete performance"] = df2["Athlete performance"].str.replace(' h', '')

# drop columns : Athlete club, Athlete Counrty, Athlete year of birth, Athlete age Category


df2 = df2.drop(columns= ["Athlete club", 'Athlete country', 'Athlete year of birth', 'Athlete age category'])

# clean up null value 
 # print(df2[df2['Athlete age'].isna()])
df2 = df2.dropna()
# check toltal null
 # print(df2.isna().sum())

# check duplicate
 # print(df2[df2.duplicates()])

# reset index 

df2.reset_index(drop = True)

# check type 

df2["Athlete age"] = df2["Athlete age"].astype(int)
df2["Athlete average speed"] = df2["Athlete average speed"].astype(float)

# print(df2.dtypes)

# rename columns 
# Year of event                  int64
# Event dates                   object
# Event name                    object
# Event distance/length         object
# Event number of finishers      int64
# Athlete performance           object
# Athlete gender                object
# Athlete average speed        float64
# Athlete ID                     int64
# Athlete age                    int64

df2 = df2.rename(columns = { 'Year of event' : 'race_year',
                             'Event dates' : 'race_date',
                             'Event name' : 'race_name' ,
                             'Event distance/length' : "length",
                             'Event number of finishers' : 'finish_number',
                             'Athlete performance' : 'performance' ,
                             'Athlete gender' : 'gender' , 
                             'Athlete average speed' : "avg_speed" , 
                             'Athlete ID' : 'athlete_id',
                             'Athlete age' : 'age'

})

                 
df3 = df2[['race_date','race_name','length', 'finish_number','athlete_id', 'performance', 'gender','avg_speed','age']]

# print(df3.head())

"""charts and graphs """ 

# sns.histplot(df3, x ='length', hue = 'gender') # chart 1 gender population base base on race length

# sns.displot(df3[df3['length'] == '50mi']['avg_speed']) # populations avg speed in 50 miles races 

# sns.violinplot(data = df3, x = 'length', y = 'avg_speed' , hue = 'gender', split= True , inner= 'quartz')

# sns.lmplot(data=df3, x = 'age', y = 'avg_speed', hue = 'gender' )

# plt.show()

""" Data deep dive """

# Dif in speed between male and female in 50mi,50km race

# print(df3.groupby(['length','gender'])['avg_speed'].mean())

# what age group are best in 50m race (show 20 )

# print(df3.query("length == '50mi'")
#      .groupby('age')['avg_speed']
#      .agg(['mean','count'])
#      .sort_values('mean', ascending = False)
#      .query('count > 19'))

# what age group are the worst (show 10)

# print(df3.query("length == '50mi'")
#      .groupby('age')['avg_speed']
#      .agg(['mean','count'])
#      .sort_values('mean', ascending = True)
#      .query('count > 9'))

# race out put base on season 

df3['race_month'] = df3['race_date'].str.split('.').str.get(1).astype(int)

df3['season'] = df3['race_month'].apply(lambda x : "winter" if x > 11 
                                                else "fall" if  x > 8
                                                else "summer" if x > 5
                                                else 'spring' if x > 2 
                                                else 'winter')


# print(df3.groupby('season')['avg_speed'].agg(['mean','count']).sort_values('mean', ascending = False))

# race out put base on season only in 50mi

print(df3.query('length == "50mi" ').groupby('season')['avg_speed'].agg(['mean','count']).sort_values('mean', ascending = False))

# print(df3.head()) 
