from fastapi import FastAPI, HTTPException
from models import Property, PropertyCreate, PropertyUpdate, PropertyList
import crud

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to Property Management API"}

@app.post("/create_new_property", response_model=Property)
async def create_new_property(property: PropertyCreate):
    new_property = await crud.create_new_property(property)
    return new_property

@app.get("/fetch_property_details", response_model=PropertyList)
async def fetch_property_details(city: str):
    properties = await crud.fetch_property_details(city)
    if not properties:
        raise HTTPException(status_code=404, detail="No properties found")
    return {"properties": properties}

@app.put("/update_property_details", response_model=Property)
async def update_property_details(property: PropertyUpdate):
    updated_property = await crud.update_property_details(property.property_id, property)
    if not updated_property:
        raise HTTPException(status_code=404, detail="Property not found")
    return updated_property

@app.get("/find_cities_by_state")
async def find_cities_by_state(state: str):
    cities = await crud.find_cities_by_state(state)
    return {"cities": cities}

@app.get("/find_similar_properties", response_model=PropertyList)
async def find_similar_properties(property_id: str):
    properties = await crud.find_similar_properties(property_id)
    if not properties:
        raise HTTPException(status_code=404, detail="Property not found")
    return {"properties": properties}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
