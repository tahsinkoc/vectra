from sentence_transformers import SentenceTransformer
import numpy as np
model = SentenceTransformer('./local_emb_model')

# text = "Bu bir örnek metindir."
# embedding = model.encode(text)

# print(embedding)  # Numpy array (boyut: 384)

def create_embedding(text:str) -> np.ndarray:

    return model.encode(text)