import pandas as pd
import numpy as np
from tqdm import tqdm

# Define paths
METADATA_FILE = 'food-101/dish_metadata.csv'

# Load metadata
df = pd.read_csv(METADATA_FILE)

# Load text embeddings
text_embeddings = []
for path in tqdm(df['text_embedding_path'], desc="Loading text embeddings"):
    embedding = np.load(path)
    text_embeddings.append(embedding)

text_embeddings = np.array(text_embeddings)
print(f"Loaded {text_embeddings.shape[0]} text embeddings with dimension {text_embeddings.shape[1]}")