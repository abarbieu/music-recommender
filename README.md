# CSC 466 Final Project - Music Recommender

## Group Members
1. Aidan Barbieux - abarbieu@calpoly.edu
2. Matthew Jaojocco - mjaojoco@calpoly.edu
3. Taylor Bedrosian - tbedrosi@calpoly.edu
4. Zachary Krogman - zkrogman@calpoly.edu

## Instructions 

### Clustering.ipynb
    A jupyter notebook that when ran produces the dendrogram of the top 200 artists by listeners on last.fm, 
    clustered by user-generated tags.
    
### countryPredictor.py
    python3 countryPredictor.py <k-value>
    Given a k-value for KNN, calculates the accuracy of predicting a user's country by the artists they listen to on last.fm. Note that lastfm.csv should be in the running directory.

### countryPredictor2.py
    python3 countryPredictor2.py <k-value>
    Same as above, but calculates the accuracy of predicting a user's location based on 9 regional buckets instead, and calculates
    the confusion matrix and accuracy of the whole dataset based on the regional buckets, 
    as well as the precision and recall for each bucket.

### music-recommender.ipynb
    A jupyter notebook using python3. Contains the implementation of our music recommender using collaborative filtering.
    