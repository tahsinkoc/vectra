from pydantic import BaseModel
from typing import List, Optional

class Vector(BaseModel):
    id: Optional[str]
    name: str
    metadataId: str
    metadata: str
    vector: List[float]
