import pandas as pd

# Load metadata
df = pd.read_csv('food-101/dish_metadata_with_clusters.csv')

# Print unique dish names per cluster
for cluster_id in range(10):  # Assuming 10 clusters
    unique_dishes = df[df['cluster_label'] == cluster_id]['cleaned_dish_name'].unique()
    print(f"Cluster {cluster_id} unique dishes: {unique_dishes}")
