from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def anything():
    return {"message": "Hello, John! This is FastAPI."}
