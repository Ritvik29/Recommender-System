# Recommendation System(RecSys) Modelling

## Running Instructions
1) The main code file is in the jupyter notebook RecSys2.ipynb. Run this
code to generate the similarity metrices for historical data.
2) To run the web service app. run the command
python app.py  
from inside the directory

## Methodology
The Following Methodology was followed to implement the recommender system-

1) The clicks data was split into training and testing dataset with 95% training data and 5% testing data.
the clicks data was merged with the stores data and the users data to create a unified training data
for the ML model.

2) A cosine similarity is computed between users using cleaned text features from the stores and users database. This gives an array of similar users sorted by similarity, from highest similarity to lowest similarity.

3) calculate counts for a user-merchant combination. This is calculated by calculating the number of occurences of a 'user_id - merchant' combination in the views dataset. this metric counts the number of times a user visits a particular merchant. 

4) So after following the above steps, we Have two matrices a) A similarity matrix for users, and a user-marchant count matrrix. Let this be called the 'favorite merchant'. The user-merchant count matrix contains the most commonly visited merchant for a particular user. and b) The similarity matrix for users which ranks users according to similarity.


5)The deployed recommender system makes use of both these matrices. For a given user_id n, performs the following steps - 
a) Check if the user n has a favorite merchant. If x is the favorite merchant, return x.
b) If condition a is not met, take the neighbor (in terms of similarity) of n, and check his favorite merchant. Keep traveling 
along the list of neighbors (from most similar to least similar) till one
of the neighbor has a favorite merchant.

6) If the conditions in 5 are not met, return the most popular merchant. This is the most frequently occurring merchant in the views dataset.

## Evaluation metrics.
This problem is evaluated like a multiclass problem, where the merchant_id is the target variable. The weighted average precision and recall scores are used at an aggregate level. 
A Dataframe of precision and recall scores is also computed for each merchant_id. Some merchant ids that received high scores in both  precision and recall include the merchant_id 1 and merchant_id 2. 


## Deployment to Heroku.
The web application is deployed on HEROKU at the given link. For a particular user_id, the application is able to predict the 
merchant_id. 






