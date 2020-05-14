# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 09:45:36 2020

@author: Tanguy
"""
from math import sqrt
import pandas as pd
from csv import reader




#---------------------------------------------------------------------------#
# Pour modifier le comportement de l'algorithme nou purrions utiliser 
# d'autres types de calcul de distance ex Minkowski , Manhattan ...
def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (float(row1[i]) - float(row2[i]))**2
	return sqrt(distance)
#--------------------------------------------------------------------------#
def find_neighbors(dataset, test_value, k):
	distances = list()
	for i in dataset:
		dist = euclidean_distance(test_value, i)
		distances.append((i, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(k):
		neighbors.append(distances[i][0])
	return neighbors
#--------------------------------------------------------------------------#
def predict(dataset, test_value, k):
	neighbors = find_neighbors(dataset, test_value, k)
	values = [row[-1] for row in neighbors]
	prediction = max(set(values), key=values.count)
	return prediction

#---------------------------------------------------------------------------#
    

dataset= list()
with open('iris.csv', 'r') as file:
    csv_reader = reader(file)
    for i in csv_reader:
        dataset.append(i)
        

k = 14
	

test_predict = list()
result_list = list()
predict_list= list()
for itm in dataset:
    result_list.append(itm[-1])
    
    test_predict.append(itm[:-1])

        
        
for itm in test_predict:
    predict_list.append(predict(dataset,itm,k))
    
pd_result = pd.Series(result_list)
pd_predict = pd.Series(predict_list)

confusion = pd.crosstab(pd_result,pd_predict)