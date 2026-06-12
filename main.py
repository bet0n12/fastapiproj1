from fastapi import FastAPI
from pydantic import BaseModel
 
app = FastAPI()
 
class ChatRequest(BaseModel):
    message: str
 
@app.get("/")
def root():
    return {"message": "Oylan assistant is running!"}

@app.get("/health")
def health():
    return {"status": "ok"}
 
@app.post("/chat")
def chat(req: ChatRequest):
    # пока возвращаем эхо; настоящий Oylan подключим позже
    return {"reply": f"You said: {req.message}"}

class PCConfigRequest(BaseModel):
    budget: int
    target_games: str
    current_specs: str

@app.post("/sendmessage")
def send_message(req: ChatRequest):
    return {
        "status": "sent",
        "message": req.message
    }

@app.get("/user/location")
def get_user_location():
    return {
        "city": "Almaty",
        "country": "Kazakhstan"
    }

@app.post("/assistant/pc_config")
def analyze_pc_config(req: PCConfigRequest):
    return {
        "status": "analyzed",
        "received_budget": req.budget,
        "games": req.target_games,
        "specs": req.current_specs,
        "ai_suggestion": "Oylan will analyze your requirements and suggest optimal PC components within your budget."
    }
