from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Payload(BaseModel):
    text: str

@app.post("/receive")
def receive(payload: Payload):
    print("Received:", payload.text)
    return {"status": "ok", "received": payload.text}
