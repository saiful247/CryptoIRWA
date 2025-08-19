from google import genai
import os

client = genai.Client(api_key="AIzaSyDn5dI5KSELZ6ONs0fTFsDFKBe3AI6xuN4")

resp = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="best agentic framework",
)
print(resp.text)
