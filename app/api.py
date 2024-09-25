from typing import Literal
from fastapi import APIRouter, File, UploadFile, Form
from PIL import Image
from app.llm import chat_suggestion

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/suggestion")
async def suggest(
    mbti_type: Literal[
        "ESTJ",
        "ENTJ",
        "ESFJ",
        "ENFJ",
        "ISTJ",
        "ISFJ",
        "INTJ",
        "INFJ",
        "ESTP",
        "ESFP",
        "ENTP",
        "ENFP",
        "ISTP",
        "ISFP",
        "INTP",
        "INFP",
    ] = Form(...),
    image: UploadFile = File(...),
):
    # Open the image using PIL
    pil_image = Image.open(image.file)

    # Call the chat_suggestion function with the image and MBTI type
    suggestion = chat_suggestion(pil_image, mbti_type)

    return {"suggestion": suggestion}
