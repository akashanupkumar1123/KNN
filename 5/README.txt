KNN - K Nearest Neighbors - Classification
To understand KNN for classification, we'll work with a simple dataset representing gene expression levels. Gene expression levels are calculated by the ratio between the expression of the target gene (i.e., the gene of interest) and the expression of one or more reference genes (often household genes). This dataset is synthetic and specifically designed to show some of the strengths and limitations of using KNN for Classification.



Elbow Method for Choosing Reasonable K Values
NOTE: This uses the test set for the hyperparameter selection of K.


Full Cross Validation Grid Search for K Value
Creating a Pipeline to find K value
Follow along very carefully here! We use very specific string codes AND variable names here so that everything matches up correctly. This is not a case where you can easily swap out variable names for whatever you want!

We'll use a Pipeline object to set up a workflow of operations:

Scale Data
Create Model on Scaled Data
How does the Scaler work inside a Pipeline with CV? Is scikit-learn "smart" enough to understand .fit() on train vs .transform() on train and test?*

*Yes! Scikit-Learn's pipeline is well suited for this! Full Info in Documentation *

When you use the StandardScaler as a step inside a Pipeline then scikit-learn will internally do the job for you.

What happens can be discribed as follows:

Step 0: The data are split into TRAINING data and TEST data according to the cv parameter that you specified in the GridSearchCV.
Step 1: the scaler is fitted on the TRAINING data
Step 2: the scaler transforms TRAINING data
Step 3: the models are fitted/trained using the transformed TRAINING data
Step 4: the scaler is used to transform the TEST data
Step 5: the trained models predict using the transformed TEST data



Note: If your parameter grid is going inside a PipeLine, your parameter name needs to be specified in the following manner:*

chosen_string_name + two underscores + parameter key name
model_name + __ + parameter name
knn_model + __ + n_neighbors
knn_model__n_neighbors
StackOverflow on this

The reason we have to do this is because it let's scikit-learn know what operation in the pipeline these parameters are related to (otherwise it might think n_neighbors was a parameter in the scaler).



Final Model
We just saw that our GridSearch recommends a K=14 (in line with our alternative Elbow Method). Let's now use the PipeLine again, but this time, no need to do a grid search, instead we will evaluate on our hold-out Test Set.