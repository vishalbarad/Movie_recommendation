# Movie_recommendation

This project is a part of the Machine learning see live project by clicking this link https://moviesimilar.herokuapp.com

<img src='movie_recommendation.gif' width="80%" height="80%">

#### -- Project Status: [Completed]

## Project Intro/Objective
The purpose of this project is to recommend top 10 similar movies which user watched before.

### Methods Used
* Data gathering
* Data preprocessing
* Machine Learning
* Model evaluation
* Predictive Modeling
* Model deploying

### Technologies
* Python
* Numpy 
* Pandas
* jupyter
* joblib
* HTML
* CSS
* JavaScript
* Flask
* Heroku
* Pycharm

## Project Description
This is project based on 'model based collborative filering' ml algorithm. Model used in this was 'NearestNeighbors' unsupervised algorithm. Here 'cosine similarity' distance measure is used to detects similar user.
Dataset used by this project is 'movies.csv' and 'ratings.csv' downloaded from movielens dataset 'https://grouplens.org/datasets/movielens/latest/'. After downloading and importing dataset(in jupyter Notebook) i did data cleaning first like dropping some unnecessary columns, handling missing values, Merging two datasets 'movie' and 'rating' on 'movieId'.
After that i just created 'pivot table' and then 'sparse matrix'.
After that i just fitted 'sparse matrix' using 'NearestNeighbors' model.
After that i just used 'kneighbors()'(which returns distance and indices) method of 'nearestneighbor' model to predict the similar user.
At last i just predicted top 10 similar movies.

## Needs of this project

- frontend developers
- data exploration/descriptive statistics
- data processing/cleaning
- statistical modeling
- writeup/reporting

## Contact
* Feel free to contact me any questions or if you are interested in contributing!


<h1 align=center>Thank You</h1>

