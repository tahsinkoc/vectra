from api.db.mongo import db
import numpy as np
from api.models.vector import Vector
from api.schemas.vectors import SearchVector
from embedding.create_embedding import create_embedding
from fastapi import HTTPException, Request
from embedding.create_hnsw_index import search_index
from api.services.api_key_service import confirm_api_key

# async def search_vector(vector: SearchVector):
#     embedding = create_embedding(vector.metadata)
#     labels, distances = search_index(embedding.tolist(), 3)

#     label = int(labels[0])

#     result = db.trips.find_one({"id": label}, {"_id": 0})
#     print(type(label))
#     if not result:
#         raise HTTPException(status_code=404, detail="Trip not found in database.")
    
#     result["distance"] = float(distances[0])
#     return result

async def search_vector(vector: SearchVector, Request: Request):

    header = Request.headers.get("API-Key")
    confirm = confirm_api_key(header)
    if confirm:
        embedding = create_embedding(vector.metadata)
        labels, distances = search_index(embedding.tolist(), 3)

        label_ids = [int(label) for label in labels]
        distance_map = {int(label): float(distance) for label, distance in zip(labels, distances)}

        results = list(db.trips.find({"id": {"$in": label_ids}}, {"_id": 0}))

        if not results:
            raise HTTPException(status_code=404, detail="Trips not found in database.")

        for result in results:
            result["distance"] = distance_map.get(result["id"], None)

        results.sort(key=lambda r: r["distance"])

        return results


async def search_vector_response_with_id(vector: SearchVector, Request: Request):
    header = Request.headers.get("API-Key")
    confirm = confirm_api_key(header)
    if confirm:
        embedding = create_embedding(vector.metadata)
        labels, distances = search_index(embedding.tolist(), 3)
        label_ids = [int(label) for label in labels]
        distance_map = {int(label): float(distance) for label, distance in zip(labels, distances)}
        return distance_map

