# K-Means Clustering
This program was designed to generate random datasets to cluster data points using K-means clustering.

# Inputs

The following variables within the make_blobs() function are able to be manipulated:  
  1) Number of samples
  
        a. Amount of points generated
  2) Centers
  
        a. Amount of centers generated
  3) Cluster S.D.
  
        a. Sets a standard deviation to the clusters
  4) Random state
  
        a. Randomly sets the centroid location 

Also, if you wish to add more parameters, check out the k-means clustering documentation within sklearn.
 
# Operation Performed

This program uses the KMeans module within sklearn.cluster to use the algorithm to perform the operation.

When adjusting the 'n_samples' in make_blobs(), you must also adjust the size of 'n_clusters' within KMeans
to match the amount of clusters made by make_blobs() and predicted by KMeans.

# Output

After running, the program has 3 different outputs: 
  1) A plot is shown with the random data points plotted, without clustering
  2) After the first, a plot is then shown with the data points in their respective clusters
  3) The centroids are then printed with their exact point location

# Tips

If using more/less than 4 clusters, make sure to adjust the plot by adding/subtracting those points by
simply following the pattern of the last 4.

Example with 4 points:

    plt.scatter(data[y_kmeans == 0, 0], data[y_kmeans == 0, 1], s = 50, color = 'red')
    plt.scatter(data[y_kmeans == 1, 0], data[y_kmeans == 1, 1], s = 50, color = 'cyan')
    plt.scatter(data[y_kmeans == 2, 0], data[y_kmeans == 2, 1], s = 50, color = 'green')
    plt.scatter(data[y_kmeans == 3, 0], data[y_kmeans == 3, 1], s = 50, color = 'yellow')
    
    plt.scatter(centers[0][0], centers[0][1], marker = '*', s = 200, color = 'black')
    plt.scatter(centers[1][0], centers[1][1], marker = '*', s = 200, color = 'black')
    plt.scatter(centers[2][0], centers[2][1], marker = '*', s = 200, color = 'black')
    plt.scatter(centers[3][0], centers[3][1], marker = '*', s = 200, color = 'black')
    
Adjusted with 3 points:

    plt.scatter(data[y_kmeans == 0, 0], data[y_kmeans == 0, 1], s = 50, color = 'red')
    plt.scatter(data[y_kmeans == 1, 0], data[y_kmeans == 1, 1], s = 50, color = 'cyan')
    plt.scatter(data[y_kmeans == 2, 0], data[y_kmeans == 2, 1], s = 50, color = 'green')
    
    plt.scatter(centers[0][0], centers[0][1], marker = '*', s = 200, color = 'black')
    plt.scatter(centers[1][0], centers[1][1], marker = '*', s = 200, color = 'black')
    plt.scatter(centers[2][0], centers[2][1], marker = '*', s = 200, color = 'black')


# How to Run
  To edit, use the text editor of your liking and run by simply using the following command in terminal/cmd:
  
    python kmeans.py
    
    
# What I Learned
  • Exposed to an abundance of Python concepts that really gave me a feeling for the language
  
  • Fundamental Python imports
