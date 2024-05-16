

# schemas.py

from pydantic import BaseModel
from typing import List
from typing import Optional

class PropertyBase(BaseModel):
    property_id: str
    name: str
    address: str
    city: str
    state: str

class PropertyCreate(PropertyBase):
    pass

class PropertyUpdate(PropertyBase):
    property_id: str

class PropertyList(BaseModel):
    properties: List[PropertyBase]
