from services.gemini_client import GeminiClient
from utils.resume_metadata import extract_contact_info
from datetime import date


class CoverLetterGenerator:

    def __init__(self):
        self.client = GeminiClient()

    def generate(self, resume_text, job_description):

        contact = extract_contact_info(resume_text)

        today = date.today().strftime("%B %d, %Y")

        prompt = f"""
Write a professional cover letter.

Candidate:
Name: {contact["name"]}
Email: {contact["email"]}
Phone: {contact["phone"]}

Date: {today}

Resume:
{resume_text}

Job Description:
{job_description}

Write 200-300 words.
"""

        return self.client.generate(prompt)