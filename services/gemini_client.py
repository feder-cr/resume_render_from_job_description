from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

class GeminiClient:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        self.client = genai.Client(api_key=api_key)

        self.model = "gemini-2.5-flash-lite"


    def generate(self, prompt):

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text