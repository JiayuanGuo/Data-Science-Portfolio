# K-NN Algorithm
Homework #4 from SEDS (offered by DIRECT, an Advanced Data Science Program )

### Contents
1. Create a `.py` file called `knn.py` that contains your own implementation of a k-NN classifier. 
 * A wrapping function that is the primary way of interacting with your code.  It takes as parameters, a training dataframe, a value of k and some input data to be classified. It returns the classification for the input data.
 * A function that returns the Euclidean distance between a row in the intput data to be classified.
 * A function that returns the list of sorted Euclidean distances between the input data and all rows in the dataframe. 
 * A function that returns the class prediction based on the list of sorted Euclidean distances.
 * A wrapping function that helps the user decide on what `k` to use.  This function takes as parameters, a training dataframe, a testing dataframe and a list of values of `k` to try. It returns a dictionary with `k` as the keys and the training accuracy of the test set.  Accuracy is measured by percentage of classifications that were correct for that value of `k`.
2. A Jupyter Notebook that documents how to use my k-NN functions in `knn.py` with an example.  Use the [`atomradii.csv`](https://uwdirect.github.io/SEDS_content/atomradii.csv) and [`testing.csv`](https://uwdirect.github.io/SEDS_content/testing.csv) that relates atomic radii to atomic class.
3. Create unit tests and put them in `test_knn.py` and use the `atomradii` data for the unit tests. Paste the output of running nosetests below. 

### Results of unit tests
```
$ nosetests
.....E
======================================================================
ERROR: test_knn.test_k_accuracy
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\users\jiayuan\miniconda3\lib\site-packages\nose\case.py", line 198, in runTest
    self.test(*self.arg)
  File "C:\Users\Jiayuan\Desktop\2017 Winter  Quarter\UW DIRECT Program\SEDS-HW\seds-hw4-coding-and-testing-big-league-JiayuanGuo\test_knn.py", line 47, in test_k_accuracy
    assert type(knn.k_accuracy()) == dict,"The output type is wrong"
  File "C:\Users\Jiayuan\Desktop\2017 Winter  Quarter\UW DIRECT Program\SEDS-HW\seds-hw4-coding-and-testing-big-league-JiayuanGuo\knn.py", line 88, in k_accuracy
    for i in range(1,len(training_data)+1):
NameError: name 'training_data' is not defined

----------------------------------------------------------------------
Ran 6 tests in 1.372s

FAILED (errors=1)

There is an error of my last unit test (test_k_accuracy function). 
I have added "knn." before all the functions and tried many times but still generate "NameError:name'training_data' is not defined". Only this unit test generate this error and I cannot make it till now.
```
