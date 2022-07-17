# USA car accidents analysis
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ishandandekar/USA-accidents-analysis/blob/main/analysis.ipynb)
<p align="center">
    <img width=300 height=170 src="assets/Kowalski.jpg">
</p>

👋 Hello and welcome to the USA car accidents analysis repository. This is my first tabular data analysis project using Python. Hope you like it!
Check out the [Medium](https://medium.com/@ishandandekar/foodvision-3843f38be45e) article as a supplement to this README.

## Introduction
I did this project to learn the skill of exploratory data analysis. EDA or Exploratory Data Analysis is an important step before predicting variables using machine learning. It helps us identify important features using graphical representation, detection of anomalies, testing of hypotheses etc. In other words, EDA is a data exploration technique to understand aspects of data.  

In this project I have analysed the accidents occured in USA (United States of America) since 2016-2021, to gain insights and draw conclusions by questioning the data and finding answers.

## Data
The data is originally collected using various APIs that provide streaming by a variety of enities, such as the US and state departments of transportation, law enforcemnt agencies, traffi cameras, and traffic sensors within the road-networks. Although for this project I have the data already available on [Kaggle](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents). The data has a total of **2.8 million accident records** with **2845342 rows and 47 columns** which was collected from **February 2016** to **December 2021**.  
To get the data on local machine I used the [**`opendatasets`**](https://github.com/JovianML/opendatasets) library, which uses the Kaggle API keys to download the data easily on your system.

## Insights
<p align="center">
    <img width=600 height=280 src="assets/myimage.png">
</p>
The data contained lots of NA values, around 3414350 of them. The analysis was mostly focused on the geolocation of the accidents, weather conditions and severity of an accident.  
While analysing the cities column I found out that Miami had the most number of accidents, followed by Los Angeles and Orlando. These cities are often the places where tourists go. 

## Tools and libraries
* Python
* Kaggle
* Jupyter notebook
* Pandas
* Matplotlib
* Plotly
* Git
* Opendatasets

## Contents of the repository
* *assets*: This folder contains the images of plots and other supporting material used to make this README file and the Medium article.
* *.gitignore*: This file is used to omit the tracking of unwanted files, so that they are not present in the repository while presenting.
* *analysis.ipynb*: This is the original jupyter notebook used for the analysis. The notebook has three parts, which include donwloading the data, cleaning the data and then finally analysis of data. The notebook also has the original plots which helped the analysis and making the README.
* *README.md*: This is a markdown file which is used to document the project, to make people understand this project better. This file is displayed on the Github repository as well.
* *requirements.txt*: As the convention goes, this file can be used to replicate the `conda` environment used to run the jupyter notebook.


A special thanks to [Aakash Rao N S](https://jovian.ai/aakashns) for this project.