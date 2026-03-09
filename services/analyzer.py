import re


class Analyzer:

    def match_score(self, resume, job):

        resume_words = set(re.findall(r"\w+", resume.lower()))
        job_words = set(re.findall(r"\w+", job.lower()))

        score = len(resume_words & job_words) / len(job_words) * 100

        return int(score)


    def keyword_analysis(self, resume, job):

        resume_words = set(resume.lower().split())
        job_words = set(job.lower().split())

        missing = job_words - resume_words

        return list(missing)[:20]