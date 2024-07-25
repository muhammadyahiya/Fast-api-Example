from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world from FastAPI"}

@app.get("/demo")
def demo_function():
    return {"message": "This is output from demo function"}

@app.post("/post_demo")
def demo_post():
    return {"message": "This is output from post demo function"}