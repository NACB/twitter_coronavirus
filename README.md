# Coronavirus twitter analysis

Programs for scanning all geotagged tweets sent in 2020 to monitor for the spread of the coronavirus on social media.

**Learning Objectives:**

This assignment, for CMC's CSCI046 class, was designed to teach us to:
1. work with large scale datasets
1. work with multilingual text
1. use the MapReduce divide-and-conquer paradigm to create parallel code

## Background

**About the Data:**

The dataset for this project contains all geotagged tweets that were sent in 2020.
In total, there are about 1.1 billion tweets in this dataset.

The tweets are stored as follows:
The tweets for each day are stored in a zip file.
Inside this zip file are 24 text files, one for each hour of the day.
Each text file contains a single tweet per line in JSON format.

**About MapReduce:**

I followed the [MapReduce](https://en.wikipedia.org/wiki/MapReduce) procedure to analyze these tweets.
It is a 3 step procedure summarized in the following image:

<img src=mapreduce.png width=100% />

## Core Visualizations

The following graphs illustrate total use of certain covid-related hashtags:
1. **#Coronavirus by Country**
<img src=coronavirus_country.png width=100% />
This first graph shows the total use of "#Coronavirus," broken down by the country tweets are sent from.

2.  **#Coronavirus by Language**
<img src=coronavirus_language.png width=100% />
This graph shows the total use of "#Coronavirus" broken down by what language a tweet was sent in.

3. **#코로나바이러스 by Country**
<img src=코로나바이러스_country.png width=100% />
This graph shows the total use of the Korean-language equivalent of #Coronavirus broken down by country

4. **#코로나바이러스 by Language**
<img src=코로나바이러스_language.png width=100% />
This graph shows the total use of the Korean-language equivalent of #Coronavirus broken down by language.

## Alternative Reduce + Visualization

I also developed `alternative_reduce.py`, which allows the user to input multiple hashtags and graphs them on a shared plot. 

Curious to see potential trends in less-primary hashtags, I ran the program on "#sick," "#doctor," and "#hospital." The trends were far less strong than expected. 

<img src=hashtag_use_final.png width=100% />

#sick saw little change over the year, with a spike in daily uses toward the end. #doctor and #hospital both declined mildly on average in daily use, save for an enormous spike in the use of #doctor around June.
