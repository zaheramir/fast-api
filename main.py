from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "message": "FastAPI server is running"}

@app.post("/receive")
def receive(data: dict):
    return {"received": data}
