Due to the simplicity of KNN for Classification, let's focus on using a PipeLine and a GridSearchCV tool, since these skills can be generalized for any model.


The Sonar Data
Detecting a Rock or a Mine
Sonar (sound navigation ranging) is a technique that uses sound propagation (usually underwater, as in submarine navigation) to navigate, communicate with or detect objects on or under the surface of the water, such as other vessels.


The data set contains the response metrics for 60 separate sonar frequencies sent out against a known mine field (and known rocks). These frequencies are then labeled with the known object they were beaming the sound at (either a rock or a mine).


Our main goal is to create a machine learning model capable of detecting the difference between a rock or a mine based on the response of the 60 separate sonar frequencies.




Train | Test Split
Our approach here will be one of using Cross Validation on 90% of the dataset, and then judging our results on a final test set of 10% to evaluate our model.

TASK: Split the data into features and labels, and then split into a training set and test set, with 90% for Cross-Validation training, and 10% for a final test set.

TASK: Create a PipeLine that contains both a StandardScaler and a KNN model



TASK: Perform a grid-search with the pipeline to test various values of k and report back the best performing parameters.


(HARD) TASK: Using the .cv_results_ dictionary, see if you can create a plot of the mean test scores per K value.


Final Model Evaluation
TASK: Using the grid classifier object from the previous step, get a final performance classification report and confusion matrix.






