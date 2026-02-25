from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

pregunta = input("¿Qué quieres preguntarle a Gemini?: ")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=pregunta,
)

print(response.text)