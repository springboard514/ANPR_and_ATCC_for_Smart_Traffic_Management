##################################################################################
# Attempting to recognize number plate characters using vision-based LLM models  #
##################################################################################

from groq import Groq
import base64
from dotenv import load_dotenv

load_dotenv()

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


# Path to your image
image_path = "D:\infosys_intern\STMS\data\ss2.png"

# Getting the base64 string  
base64_image = encode_image(image_path)

print(base64_image)

client = Groq()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "extract the characters of the given number plate and just return it to me."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ],
    model="llama-3.2-90b-vision-preview",
)

print(chat_completion.choices[0].message.content)