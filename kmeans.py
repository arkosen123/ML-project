import math
import random

import numpy as np


def euclidean_distance(sample1, sample2):
    distance = 0
    for i in range(len(sample1)):
        distance += (sample1[i] - sample2[i]) ** 2
    return math.sqrt(distance)


def find_centroids(dataset, clusters):
    classes = {}
    centroids = []
    for i in range(len(clusters)):
        if clusters[i] in classes.keys():
            classes[clusters[i]].append(dataset[i])
        else:
            classes[clusters[i]] = [dataset[i]]
    print("CLASSES", classes)
    for class_label in classes.keys():
        points = classes[class_label]
        print("POINTS", points)
        centroid = np.mean(points, axis=0)
        print("CENTROID", centroid)
        centroids.append(centroid)

    return centroids




def k_means_clustering(dataset, k):
    m = dataset.shape[0]
    n = dataset.shape[1]
    centroids = dataset[random.sample(range(m), k,)]
    n_iter = 10
    for iter in range(n_iter):
        clusters = []
        print(centroids)
        prev_centroids = centroids.copy()
        for idx, point in enumerate(dataset):
            distances = []

            for centroid_idx, centroid in enumerate(centroids):
                distances.append((euclidean_distance(point, centroid), centroid_idx))
            sorted_distances = sorted(distances)
            nearest_centroid = sorted_distances[0]
            nearest_centroid_cluster = nearest_centroid[1]
            clusters.append(nearest_centroid_cluster)

        centroids = find_centroids(dataset, clusters)
        print("CLUSTERS", clusters)
        
