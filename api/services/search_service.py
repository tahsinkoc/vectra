from api.db.mongo import db
import numpy as np
from api.models.vector import Vector
from api.schemas.vectors import SearchVector
from embedding.create_embedding import create_embedding
from fastapi import HTTPException
from embedding.create_hnsw_index import search_index

async def search_vector(vector: SearchVector):
    embedding = create_embedding(vector.metadata)
    labels, distances = search_index(embedding.tolist(), 3)

    label = int(labels[0])

    result = db.trips.find_one({"id": label}, {"_id": 0})
    print(type(label))
    if not result:
        raise HTTPException(status_code=404, detail="Trip not found in database.")
    
    result["distance"] = float(distances[0])
    return result
