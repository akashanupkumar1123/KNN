we’ll learn to implement K-Nearest Neighbors from Scratch in Python. KNN is a Supervised algorithm that can be used for both classification and regression tasks.

KNN is very simple to implement. In this article, we will implement the KNN algorithm from scratch to perform a classification task.

The intuition behind the K-Nearest Neighbors Algorithm
In K-Nearest Neighbors there is no learning required as the model stores the entire dataset and classifies data points based on the points that are similar to it. It makes predictions based on the training data only.



Consider the figure above. There are two classes of data (Red and Green) and we were given a new data point (black) and asked to specify which class does this new datapoint belongs to?

Well, KNN drives on the notion that similar items tend to be closer in groups. So it is quite evident that the new data point is closer to the red group and hence the algorithm will classify this point as Red



Ways to calculate the distance in KNN:

Manhattan Method
Euclidean Method
Minkowski Method
mahalanobis distance
etc..

Implementing K-Nearest Neighbors from Scratch in Python
First we will figure out the steps involved in the implementation of K-Nearest Neighbors from Scratch.

Step 1. Figure out an appropriate distance metric to calculate the distance between the data points.

Step 2. Store the distance in an array and sort it according to the ascending order of their distances (preserving the index i.e. can use NumPy argsort method).

Step 3. Select the first K elements in the sorted list.

Step 4. Perform the majority Voting and the class with the maximum number of occurrences will be assigned as the new class for the data point to be classified.










