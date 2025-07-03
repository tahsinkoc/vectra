from api.db.mongo import db
from api.models.vector import Vector
from api.schemas.vectors import CreateVector
from api.services.api_key_service import confirm_api_key
from embedding.create_embedding import create_embedding
from fastapi import HTTPException, Request
from embedding.create_hnsw_index import create_index

async def create_vector(vectora: CreateVector, Request: Request):

    header = Request.headers.get("API-Key")

    confirm = confirm_api_key(header)    
    if confirm:
        find = db.vectors.find_one({
        "$or": [
            {"metadataId": vectora.id},
            {"numericId": vectora.numericId}
        ]
        })
        if find:
            raise HTTPException(status_code=400, detail="Vector already exists")
        embedding = create_embedding(vectora.metadata)
        index = create_index(embedding.tolist(), vectora.numericId)
        print(index)
        newvector = Vector(
        id=None,
        name=vectora.name,
        metadataId = vectora.id,
        metadata = vectora.metadata,
        vector= embedding,
        numericId = vectora.numericId
    )
        result = db.vectors.insert_one(newvector.model_dump())
        return {"inserted_id": str(result.inserted_id)}

    