from google import genai
from PIL import Image
import io

client = genai.Client(api_key="AIzaSyClP8R_WbucRbiqCH9rlkfTC8u6tDJyPL8")

def gemini_analyzer(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    prompt="""
    You are a binary image classifier.

Task:
Determine whether the image mainly shows natural soil, mud, dirt, or sand ground.

Reply YES if:
- The dominant surface is natural earth (soil, mud, dirt, or sand).
- Small natural debris like tiny roots or dry fragments are allowed.

Reply NO if:
- A human or animal is visible.
- A clear artificial surface (concrete, tiles, road, plastic, wood) is visible.
- The ground is covered mainly by grass or plants.

Rules:
- Reply with ONLY one word.
- Reply exactly: YES or NO
- Do not explain.
- Do not add punctuation.
- Do not add extra text.
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt,image]
    )
    text = response.text.strip().lower()

    return "yes" in text