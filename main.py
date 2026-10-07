from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
async def read_root():
    print("Hello")
    return {"msg": "Hello, World!"}
