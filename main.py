from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Create an instance of FastAPI
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

jsonD = [
    {
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com",
        "age": 30,
        "is_active": True
    },
    {
        "id": 2,
        "username": "jane_smith",
        "email": "jane@example.com",
        "age": 28,
        "is_active": False
    },
    {
        "id": 3,
        "username": "alice_wonder",
        "email": "alice@example.com",
        "age": 35,
        "is_active": True
    }
]


# Define a route for the GET request
@app.get("/api/data1")
async def get_data1():
    return jsonD

@app.get("/api/data2")
async def getdata2():
    return jsonD