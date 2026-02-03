from openai import OpenAI
import os 
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
import requests

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Generate and save image 

prompt = input("Enter the image description: ")
response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
)
responses = requests.get(response.data[0].url)
image = Image.open(BytesIO(responses.content))
image.show()
    