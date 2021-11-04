import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np

data = pd.read_csv('wine.csv')

data = data[['Alcohol','Magnesium']].values


def distance(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**(1/2)


def Kmean(k,data):

    centroids = []

    while len(centroids) != k:
       centroid = random.choice(data)
       if list(centroid) not in centroids:
           centroids.append(list(centroid))


    print(centroids)

    for _ in range(1000):
        clusters = [[] for i in range(k)]
        for datapoint in data:
            distances = []
            
            for i in range(k):
                distances.append(distance(datapoint[0],datapoint[1],centroids[i][0],centroids[i][1]))
            
            clusters[np.argmin(distances)].append(datapoint)

            
        for i in range(k):
            x = 0
            y = 0

            for datapoint in clusters[i]:
                x += datapoint[0]
                y += datapoint[1]

            centroids[i] = [x / len(clusters[i]), y / len(clusters[i])]

    

    return clusters,centroids


def display(clusters,centroids):
    colors = ['lime','navy', 'gold']

    for i in range(len(clusters)):
        for datapoint in clusters[i]:
            plt.plot(datapoint[0],datapoint[1],'.',color=colors[i])
        
        plt.plot(centroids[i][0],centroids[i][1],'x')

    plt.savefig('clusters.png')

clusters,centroids = Kmean(3,data)
display(clusters,centroids)


