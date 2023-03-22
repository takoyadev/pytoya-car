from fastapi import FastAPI
from models.dto import RootContentDto, CarsListDto, CarsDto

with open("./DESCRIPTION.md", "r") as description_file:
    description = description_file.read()

api = FastAPI(
    title="Takoya'Cars API",
    description=description,
    version="1.0.0",
    openapi_tags=[
        {"name":"Checks", "description":"""
All checks endpoints
         """},
        {"name":"Cars", "description":"""
All cars endpoints

You will be able to:

* **List cars**
* **Create a car** (_not implemented_)
* **Read a car** (_not implemented_)
* **Update a car** (_not implemented_)
* **Delete a car** (_not implemented_)
         """}
    ]
)


@api.get(
    path="/",
    description="Return a welcome message (usefull for manual pings)",
    tags=["Checks"]
)
async def check_root() -> RootContentDto :
    return {"message":"Welcome on Takoya'Cars API (v.python) !","version":"1.0.0"}

@api.get(
    path="/cars",
    description="List all cars from database",
    tags=["Cars"]
)
async def list_cars() -> CarsListDto :
    return CarsListDto(
        status="success",
        cars=[
            CarsDto(owner="chinjto", brand="SEAT", model="Leon III"),
            CarsDto(owner="toto", brand="PEUGEOT", model="208")
        ]
    )
