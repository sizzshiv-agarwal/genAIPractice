from google import genai
from google.genai import types
client = genai.Client(api_key='')

# Only run this block for Vertex AI API
#client = genai.Client(
 #   vertexai=True, project='988710364027', location='us-central1'

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents='Why is the sky blue?'
)
print(response.text)
