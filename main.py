from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
async def read_root():
    print("called")
    return {"msg": "Hello, World!"}
