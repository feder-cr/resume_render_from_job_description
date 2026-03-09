from services.gemini_client import GeminiClient
from prompts.prompts import RESUME_TAILOR_PROMPT


class ResumeBuilder:

    def __init__(self):
        self.llm = GeminiClient()

    def build(self, resume_text, job_description):

        prompt = RESUME_TAILOR_PROMPT.format(
            resume=resume_text,
            job_description=job_description
        )

        return self.llm.generate(prompt)