
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

def kmeans_least_confidence_samples(data, n_clusters=5, n_samples=3):
    """
    Perform K-Means clustering and identify least confidence samples in each cluster.

    :param data: DataFrame or 2D array with X, Y, Z coordinates
    :param n_clusters: Number of clusters to form
    :param n_samples: Number of least confidence samples to select from each cluster
    :return: Indices and samples of least confidence samples
    """

    # Perform K-Means Clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=0, n_init=10).fit(data)
    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    # Calculate distances of all points to their respective cluster centroids
    distances = cdist(data, centroids, 'euclidean')

    # For each cluster, find the points with the maximum distance (least confidence)
    least_confidence_samples_indices = []
    least_confidence_samples = []
    for cluster in range(n_clusters):
        cluster_distances = distances[labels == cluster, cluster]
        # Get indices of points with the maximum distance in the cluster
        indices = np.argsort(cluster_distances)[::-1][:n_samples]
        actual_indices = np.where(labels == cluster)[0][indices]
        least_confidence_samples_indices.extend(actual_indices)
        for idx in actual_indices:
            least_confidence_samples.append(data[idx])

    return least_confidence_samples_indices, least_confidence_samples

# Load the data
df = pd.read_excel('Data/compressed_data_with_noise.xlsx') # Data/Intensity_noise/compressed_data_with_intensity_noise.xlsx
data = df.iloc[:, :3].to_numpy()  # Only use the first three columns for clustering


# Use the function with the loaded data
indices, samples = kmeans_least_confidence_samples(data)

print("Least Confidence Samples with Labels:")
for idx, sample in zip(indices, samples):
    formatted_sample = ', '.join([f"{coord:.4f}" for coord in sample])  # Format coordinates to 4 decimal places
    label = df.iloc[idx, 3]  # Retrieve the label from the fourth column
    print(f"Index {idx}: [{formatted_sample}], Label: {label}")
