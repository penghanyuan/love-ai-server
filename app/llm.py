from PIL import Image
import ell
import openai
from .config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


@ell.simple(model="gpt-4o")
def chat_suggestion(image: Image.Image, mbti_type: str):
    return [
        ell.system(
            f"""
            You are a helpful assistant that provides chat suggestions based on MBTI types.
            In the image, normally the message I sent is on the right side and the message
            from the other person is on the left side. My MBTI type is {mbti_type}. You
            should first consider the characteristics of my MBTI type and provide me with
            chat suggestions. I want to have good relationships with people. Think step
            by step and provide me with only one chat suggestion. Don't include any other
            thing. It should not be longer than 30 words. Reply with the language of the
            message in the image. Use as much as possible the tone of my message in the image.
            """
        ),
        ell.user(
            [
                image,
            ]
        ),
    ]
