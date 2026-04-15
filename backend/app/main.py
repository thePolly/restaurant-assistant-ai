from fastapi import FastAPI
from pydantic import BaseModel
from reservation_flow import process_reservation_email

app = FastAPI()

class EmailRequest(BaseModel):
    message: str

@app.post("/process-email")
def process_email(request: EmailRequest):
    return process_reservation_email(request.message)