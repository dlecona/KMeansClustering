#Importing necessary libraries for K-means clustering
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

#Generating a random dataset using 'make_blobs'

dataset = make_blobs(n_samples = 200, centers = 4, 
		     cluster_std = 1.8, random_state = 20)

#just printing the dataset gives you a 2D array
#dataset[0] contains the points of all the data
#dataset[1] contains the cluster to which it belongs to

data = dataset[0]

#create a kmeans objects
kmeans = KMeans(n_clusters = 4)
#fitting the object to the randomly generated data
kmeans.fit(data)

#plots the centers (black stars) onto the data points but it is not accurate
#because the centers are not yet fitted to the data

#the ‘:’ in the ‘dataset[ 0 ][ : , 0 ] simply means to iterate through every data point within this element
plt.scatter(dataset[0][:, 0], dataset[0][:, 1])
plt.show()

#Grabbing a variable within 'kmeans' which gives us the center points of each cluster
centers = kmeans.cluster_centers_

#Printing centers of each cluster
print("Centroids:")
print(centers)


#Fitting the data points and predicting there centers
y_kmeans = kmeans.fit_predict(data)

#plotting each cluster with distinct color
plt.scatter(data[y_kmeans == 0, 0], data[y_kmeans == 0, 1], s = 50, color = 'red')
plt.scatter(data[y_kmeans == 1, 0], data[y_kmeans == 1, 1], s = 50, color = 'cyan')
plt.scatter(data[y_kmeans == 2, 0], data[y_kmeans == 2, 1], s = 50, color = 'green')
plt.scatter(data[y_kmeans == 3, 0], data[y_kmeans == 3, 1], s = 50, color = 'yellow')

#Plotting the centers of each cluster with a black star
plt.scatter(centers[0][0], centers[0][1], marker = '*', s = 200, color = 'black')
plt.scatter(centers[1][0], centers[1][1], marker = '*', s = 200, color = 'black')
plt.scatter(centers[2][0], centers[2][1], marker = '*', s = 200, color = 'black')
plt.scatter(centers[3][0], centers[3][1], marker = '*', s = 200, color = 'black')

#showing data to screen
plt.show()
