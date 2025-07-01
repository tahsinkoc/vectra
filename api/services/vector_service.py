from api.db.mongo import db
from api.models.vector import Vector
from api.schemas.vectors import CreateVector
from embedding.create_embedding import create_embedding

async def create_vector(vectora: CreateVector):
    embedding = create_embedding(vectora.metadata)
    newvector = Vector(
    id=None,
    name=vectora.name,
    metadataId = vectora.id,
    metadata = vectora.metadata,
    vector= embedding
)
    result = db.vectors.insert_one(newvector.model_dump())
    return {"inserted_id": str(result.inserted_id)}