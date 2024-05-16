from pydantic import BaseModel, Field
from typing import Optional, List
from bson import ObjectId

class Property(BaseModel):
    property_id: Optional[str] = Field(None, alias="_id")
    name: str
    address: str
    city: str
    state: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class PropertyCreate(BaseModel):
    name: str
    address: str
    city: str
    state: str

class PropertyUpdate(BaseModel):
    property_id: str
    name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None

class PropertyList(BaseModel):
    properties: List[Property]
