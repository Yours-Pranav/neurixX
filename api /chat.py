from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import openai

app = FastAPI()

# Directly using your OpenAI API key (not recommended for production)
openai.api_key = "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"

class Message(BaseModel):
    message: str

@app.post("/")
async def chat(message: Message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": message.message}
            ]
        )
        reply = response['choices'][0]['message']['content']
        return {"reply": reply}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
