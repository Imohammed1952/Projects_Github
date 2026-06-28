'''
import numpy as np
from sklearn.cluster import DBSCAN
import pandas as pd
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D



eps = 100
min = 1




# Read the data from the Excel file
df = pd.read_excel('compressed_data.xlsx')

# Convert the DataFrame to a NumPy array
data = df.to_numpy()


data.shape, data[:5]  # Show the shape of the data and the first 5 points

# Convert to NumPy array
data_array = np.array(data)

dbscan = DBSCAN(eps=eps, min_samples=min)

dbscan.fit(data_array)

cluster_labels = dbscan.labels_

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot of the data points
scatter = ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=cluster_labels, cmap='viridis')

# Title and labels
ax.set_title('3D plot of data points with DBSCAN clustering')
ax.set_xlabel('X coordinate')
ax.set_ylabel('Y coordinate')
ax.set_zlabel('Z coordinate')

# Legend
legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
ax.add_artist(legend1)

# Show plot
plt.show()'''







import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    # Load the data
    df = pd.read_excel('Data/compressed_data_with_labels.xlsx')
    data = df.iloc[:, :3].to_numpy()  # Only use the first three columns for clustering

    # Initial KMeans Clustering with explicit n_init value
    n_clusters = 5
    kmeans = KMeans(n_clusters=n_clusters, n_init=10)
    kmeans.fit(data)
    cluster_labels = kmeans.labels_

    # Visualize the initial clustering
    visualize_clusters(data, cluster_labels, title='Initial Clustering')

    # Select samples for labeling
    selected_samples = select_samples_for_labeling(data, cluster_labels, kmeans, n_clusters)

    # Manual labeling process
    labeled_samples = manual_labeling(selected_samples, df.iloc[:, 3])  # Pass the classifier column for labeling

    return selected_samples, labeled_samples

    # # Incorporate labeled samples into the model
    # new_kmeans = reinitialize_kmeans_with_labels(data, labeled_samples, n_clusters)
    # new_cluster_labels = new_kmeans.labels_

    # # Visualize the updated clustering
    # visualize_clusters(data, new_cluster_labels, title='Updated Clustering after Active Learning')

def select_samples_for_labeling(data, cluster_labels, kmeans, n_clusters, n_samples_per_cluster=5):
    selected_samples = []
    for cluster in range(n_clusters):
        # Get the indices of the data points belonging to the current cluster
        cluster_indices = np.where(cluster_labels == cluster)[0]

        # Check the number of samples in the cluster
        num_samples_in_cluster = len(cluster_indices)
        num_samples_to_select = min(n_samples_per_cluster, num_samples_in_cluster)

        # Randomly select indices from the cluster
        selected_indices = np.random.choice(cluster_indices, num_samples_to_select, replace=False)

        # Add the selected samples to the list
        for index in selected_indices:
            selected_samples.append(data[index])

    return selected_samples



def manual_labeling(selected_samples, classifier_column):
    labeled_samples = []
    for sample in selected_samples:
        print("Data point:", sample)
        actual_label = classifier_column.iloc[sample]
        print("Actual label for this sample:", actual_label)
        # In a real scenario, here you would ask for manual labeling
        # For this example, we use the actual label directly
        labeled_samples.append(actual_label)
        print("\n")
    return labeled_samples

def reinitialize_kmeans_with_labels(data, labeled_samples, n_clusters):
    # For simplicity, this example will not modify the KMeans initialization with labels
    # This can be more complex in real-world scenarios
    #TODO
    new_kmeans = KMeans(n_clusters=n_clusters, n_init=10)
    new_kmeans.fit(data)
    return new_kmeans

def visualize_clusters(data, cluster_labels, title='3D plot of data points with K-means clustering'):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=cluster_labels, cmap='viridis')
    ax.set_title(title)
    ax.set_xlabel('X coordinate')
    ax.set_ylabel('Y coordinate')
    ax.set_zlabel('Z coordinate')
    legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
    ax.add_artist(legend1)
    plt.show()

if __name__ == "__main__":
    main()

