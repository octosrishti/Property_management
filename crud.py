from models import Property, PropertyCreate, PropertyUpdate
from bson import ObjectId
from database import property_collection

async def create_new_property(property_data: PropertyCreate):
    property_dict = property_data.dict()
    result = await property_collection.insert_one(property_dict)
    property_dict["_id"] = str(result.inserted_id)
    return property_dict

async def fetch_property_details(city: str):
    properties = await property_collection.find({"city": city}).to_list(100)
    return [Property(**{**property, "_id": str(property["_id"])}) for property in properties]

async def update_property_details(property_id: str, property_data: PropertyUpdate):
    update_data = {k: v for k, v in property_data.dict().items() if v is not None}
    if "_id" in update_data:
        del update_data["_id"]
    result = await property_collection.update_one({"_id": ObjectId(property_id)}, {"$set": update_data})
    if result.matched_count:
        updated_property = await property_collection.find_one({"_id": ObjectId(property_id)})
        return Property(**updated_property)
    return None

async def find_cities_by_state(state: str):
    cities = await property_collection.distinct("city", {"state": state})
    return cities

async def find_similar_properties(property_id: str):
    property = await property_collection.find_one({"_id": ObjectId(property_id)})
    if not property:
        return None
    similar_properties = await property_collection.find({"city": property["city"], "_id": {"$ne": ObjectId(property_id)}}).to_list(100)
    return [Property(**property) for property in similar_properties]
