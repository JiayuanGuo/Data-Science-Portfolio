import numpy as np
import pandas as pd 
import math
import operator

#load our datafiles
data = pd.read_csv('atomsradii.csv')
testing = pd.read_csv('testing.csv')
#define training dataset and testing dataset
data_rWC = data.iloc[:,0].values
data_rCh = data.iloc[:,1].values
testing_rWC = testing.iloc[:,0].values
testing_rCh = testing.iloc[:,1].values
data_type = pd.DataFrame(data.iloc[:,3].values)
testing_type = pd.DataFrame(testing.iloc[:,3].values)
#combine rWC and rCh as an array
df_data = np.column_stack((data_rWC,data_rCh))
df_testing = np.column_stack((testing_rWC,testing_rCh))

def EuclideanDistance(instance1, instance2):
    """This function calculates the Euclidean distance"""
    distance = 0
    for x in range(2):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

def SortedEuclidean(test_data,training_data):
    """This function returns a sorted list containing euclidean distances from a specific test data to a row of training data, a correspond data point (defined by rWC and rCh) and its type"""
    distances = []
    for item in training_data:
        dist = EuclideanDistance(test_data,item)
        distances.append((dist,item))
        df_distances = pd.DataFrame(distances)
        d = pd.merge(df_distances,data_type,left_index=True,right_index=True,how='outer')
        d.columns = ['euclidean_distance','data_point','type']
        sorted_list = d.sort_values(by='euclidean_distance',ascending=True)
        sorted_list = sorted_list.reset_index(drop=True)
    return sorted_list


def GetNeighbors(test_data,training_data, k):
    """This function get the neighbors that returns k most similar neighbors from the training set for a given input data (using the already defined EuclideanDistance function). Create a dictionary and set different types as keys to store Neighbordata in separated lists """
    TrainingData = SortedEuclidean(test_data,training_data)
    NeighborData = TrainingData.head(k)
    #initialize dictionaries and set different types as keys
    keyDict = {'PT','TM','Alk'}
    neighbors_dict = dict([(key, []) for key in keyDict])
    for i in range(k):
        data_distance = NeighborData.iloc[i,0]
        data_type = NeighborData.iloc[i,2]
        neighbors_dict[data_type].append(data_distance) 
    #add a list containing distances and counts as the value of keys
    count_PT = len(neighbors_dict['PT'])
    count_TM = len(neighbors_dict['TM'])
    count_Alk = len(neighbors_dict['Alk'])
    neighbors_dict.setdefault('PT',[]).append(count_PT)
    neighbors_dict.setdefault('TM',[]).append(count_TM)
    neighbors_dict.setdefault('Alk',[]).append(count_Alk)
    return neighbors_dict


def ClassPrediction(test_data,training_data, k):
    """This function uses knn algorithm to predict the specific class for a given input data"""
    #Create a dictionary to extract all the counts for different types
    neighbors = GetNeighbors(test_data,training_data, k)
    count_PT = neighbors['PT'][-1]
    count_TM = neighbors['TM'][-1]
    count_Alk = neighbors['Alk'][-1]
    type_counts={'PT':count_PT,'TM':count_TM,'Alk':count_Alk}
    #Get the max value count 
    max_count = max(type_counts.values())
    result = max(type_counts,key=type_counts.get)
    return result

def accuracy(test_dataframe,test_data,training_data,k):
    """This function calculates the accuracy for a given k value"""
    correct = 0
    for i in range(len(test_dataframe)):
        if test_dataframe.iloc[i][-1] == ClassPrediction(test_data[i],training_data, k):
            correct += 1
            accuracy =(correct/float(len(test_data))) * 100
    return repr(accuracy) + "%"

def k_accuracy():
    """This function returns to a dictionary containing k value 
    and corresponding accuracy that helps the user decide on what k to use."""
    accuracy_dict={}
    for i in range(1,len(training_data)+1):
        accuracy_dict[i] = accuracy(test_dataframe,test_data,training_data,i)
    return accuracy_dict
