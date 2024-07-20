from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import torch
from transformers import pipeline, AutoModelForSeq2SeqLM,AutoTokenizer

# Create FastAPI instance
app = FastAPI()

# Load model and tokenizer
model_path = "E:\Git Uploads\English-to-Spanish-Translation-APP\notebook\results\checkpoint-28041"
model = AutoModelForSeq2SeqLM.from_pretrained(model_path).to("cuda")  
tokenizer = AutoTokenizer.from_pretrained(model_path)

# translation pipeline
translator = pipeline("translation_en_to_es", model=model, tokenizer=tokenizer)

# Define a data model
class TextToTranslate(BaseModel):
    text: str
    
templates = Jinja2Templates(directory="templates")
    
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/translate")
async def translate_text(request: Request):
    form_data = await request.form()
    text_to_translate = form_data.get("text")
    translation = translator(text_to_translate)[0]["translation_text"]
    return templates.TemplateResponse("index.html", {"request": request, "translation": translation})

