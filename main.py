from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
async def read_root():
    return {"msg": "Hello, World!"}