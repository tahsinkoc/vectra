import hnswlib
import os
import numpy as np

INDEX_PATH = './indexes/index.bin'
DIM = 384

def create_or_load_index(dim=DIM, max_elements=100000):
    index = hnswlib.Index(space='l2', dim=dim)
    if os.path.exists(INDEX_PATH):
        index.load_index(INDEX_PATH)
    else:
        index.init_index(max_elements=max_elements, ef_construction=200, M=32)
    index.set_ef(150)
    return index

def create_index(vector: list[float], id: int):
    index = create_or_load_index(dim=len(vector))
    index.add_items(np.array([vector]), np.array([id]))
    index.save_index(INDEX_PATH)
    return id

def search_index(vector: list[float], k: int):
    index = create_or_load_index(dim=len(vector))
    labels, distances = index.knn_query(np.array([vector]), k=k)
    return labels[0], distances[0]
