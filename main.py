from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def root():
    return {"endpoints": ["/get", "/post"]}


@app.get("/get")
def get():
    return {"message": "Hello World", "method": "GET"}


@app.post("/post")
def post():
    return {"message": "Hello World", "method": "POST"}


uvicorn.run(app, host="0.0.0.0", port=8080)
