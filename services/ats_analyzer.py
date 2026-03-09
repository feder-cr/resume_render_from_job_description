import re
from collections import Counter

STOPWORDS = {
    "the","a","an","and","or","if","to","of","for","in","on","with",
    "is","are","was","were","be","been","being","this","that","it",
    "as","by","at","from","about","into","over","after","before",
    "between","but","not","so","very","can","will","just","any",
    "please","how","few","more","most","other","some","such"
}


def clean_text(text: str):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    words = text.split()
    words = [w for w in words if w not in STOPWORDS and len(w) > 2]
    return words


class ATSAnalyzer:

    def analyze(self, resume_text: str, job_description: str):

        jd_words = clean_text(job_description)
        resume_words = clean_text(resume_text)

        jd_freq = Counter(jd_words)

        # Top JD keywords
        important_keywords = [w for w, _ in jd_freq.most_common(40)]

        resume_set = set(resume_words)

        matched = []
        missing = []

        for word in important_keywords:
            if word in resume_set:
                matched.append(word)
            else:
                missing.append(word)

        score = int(len(matched) / len(important_keywords) * 100)

        return {
            "score": score,
            "matched": matched,
            "missing": missing[:20]
        }