import knn

test_dataframe = knn.testing
test_data = knn.df_testing
training_data = knn.df_data

def test_EuclideanDistance():
    instance1 = [1,1]
    instance2 = [4,5]
    assert knn.EuclideanDistance(instance1, instance2) == 5, "Result of euclidean calculation is wrong"
    return

def test_SortedEulidean():
    """This function test the order of SortedEulidean function"""
    test_data = [1,1]
    training_data = knn.df_data
    assert knn.SortedEuclidean(test_data,training_data).iloc[0][0] < knn.SortedEuclidean(test_data,training_data).iloc[1][0], "The sorted order is wrong"
    return

def test_GetNeighbors():
    test_data = [0.51,1.12]
    training_data = knn.df_data
    k=3
    assert knn.GetNeighbors(test_data,training_data, k)['Alk'][-1] == 3, "Count of neighbor points is wrong"
    return

def test_ClassPrediction():
    test_data = [0.51,1.12]
    training_data = knn.df_data
    k=5
    assert knn.ClassPrediction(test_data,training_data, k) == 'Alk', "Class Prediction is wrong"
    return

def test_accuracy():
    test_dataframe = knn.testing
    test_data = knn.df_testing
    training_data = knn.df_data
    k = 3
    assert knn.accuracy(test_dataframe,test_data,training_data,k) == '60.0%', "Accuracy calculated wrong"
    return


def test_k_accuracy():
    test_dataframe = knn.testing
    test_data = knn.df_testing
    training_data = knn.df_data
    assert type(knn.k_accuracy()) == dict,"The output type is wrong"
    return
