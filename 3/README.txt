Classification and Regression

Lazy learner

Instance Based
Lazy because it does not try to learn a function from the training data.
It memorise the pattern from the dataset
Nonparametric model

distribution-free tests because no assumption of the data needing to follow a specific distribution
wikipedia
Other examples - Decision Tree, Random Forest
Used for:

Predict cancer is malignant or benign
Pattern recognition
Recommender Systems
Computer Vision
Gene Expression
Protein-Protein Interaction and 3D Structure Prediction



Disadvantages
Not efficient on big data
Curse of dimensionality. Very susceptible to overfitting


Steps:
Choose the number of  𝑘 
Select a distance metric
Find the k nearest neighbors of the sample
Assign the class label by majority vote



DistanceMetric class documentation
scikit-learn

Metrics intended for real-valued vector spaces:

identifier	class name	args	distance function
"euclidean"	EuclideanDistance		 ∑(𝑥−𝑦)2)⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯√ 
"manhattan"	ManhattanDistance		 ∑||𝑥−𝑦|| 
"chebyshev"	ChebyshevDistance		max ||𝑥−𝑦|| 
"minkowski"	MinkowskiDistance	p	 ∑(||𝑥−𝑦||𝑝)1𝑝 
"wminkowski"	WMinkowskiDistance	p, w	 ∑(𝑤||𝑥−𝑦||𝑝)1𝑝 
"seuclidean"	SEuclideanDistance	V	 ∑(𝑥−𝑦)2𝑉)⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯√ 
Refer to documentation for more on

Metrics intended for two-dimensional vector spaces

Metrics intended for integer-valued vector spaces

Metrics intended for boolean-valued vector spaces

User-defined distance

Source: Rorasa's blog

Mathematically a norm is a total size or length of all vectors in a vector space or matrices.
For simplicity, we can say that the higher the norm is, the bigger the (value in) matrix or vector is.
Norm may come in many forms and many names, including these popular name: Euclidean distance, Mean-squared Error, etc.
Most of the time you will see the norm appears in a equation like this:
‖𝑥‖ where 𝑥 can be a vector or a matrix.

Euclidean distance

Most common
L2 norm of two vectors.
In a bidimensional plane, the Euclidean distance refigures as the straight line connecting two points, and you calculate it as the square root of the sum of the squared difference between the elements of two vectors.
The Euclidean distance between points (1,2) and (3,3) can be computed (1−3)2+(2−3)2⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯√, which results in a distance of about 2.236.
Manhattan distance
Another useful measure is the Manhattan distance
L1 norm of two vectors
Summing the absolute value of the difference between the elements of the vectors.
If the Euclidean distance marks the shortest route, the Manhattan distance marks the longest route, resembling the directions of a taxi moving in a city. (The distance is also known as taxicab or city-block distance.)
For instance, the Manhattan distance between points (1,2) and (3,3) is abs(1–3) and abs(2–3), which results in 3.
Chebyshev distance
Takes the maximum of the absolute difference between the elements of the vectors.
It is a distance measure that can represent how a king moves in the game of chess or, in warehouse logistics, the operations required by an overhead crane to move a crate from one place to another.
In machine learning, the Chebyshev distance can prove useful when you have many dimensions to consider and most of them are just irrelevant or redundant (in Chebyshev, you just pick the one whose absolute difference is the largest).
In the example used in previous sections, the distance is simply 2, the max between abs(1–3) and abs(2–3).



