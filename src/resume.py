from dataclasses import dataclass, field
from typing import List, Dict
import yaml

@dataclass
class PersonalInformation:
    name: str
    surname: str
    date_of_birth: str
    country: str
    city: str
    address: str
    phone_prefix: str
    phone: str
    email: str
    github: str
    linkedin: str

@dataclass
class Exam:
    name: str
    grade: str

@dataclass
class Education:
    degree: str
    university: str
    gpa: str
    graduation_year: str
    field_of_study: str
    exam: List[Exam]

@dataclass
class Responsibility:
    description: str

@dataclass
class Experience:
    position: str
    company: str
    employment_period: str
    location: str
    industry: str
    key_responsibilities: List[Responsibility]
    skills_acquired: List[str]

@dataclass
class Project:
    name: str
    description: str
    link: str

@dataclass
class Achievement:
    name: str
    description: str

@dataclass
class Language:
    language: str
    proficiency: str

class Resume:
    def __init__(self, yaml_str: str):
        data = yaml.safe_load(yaml_str)
        self.personal_information = PersonalInformation(**data['personal_information'])
        self.education_details = [Education(
            **{k: v for k, v in edu.items() if k != 'exam'},
            exam=[Exam(name=k, grade=v) for k, v in edu['exam'].items()]
        ) for edu in data['education_details']]
        self.experience_details = [Experience(
            **{k: v for k, v in exp.items() if k not in ['key_responsibilities', 'skills_acquired']},
            key_responsibilities=[Responsibility(description=list(resp.values())[0]) for resp in exp['key_responsibilities']],
            skills_acquired=exp['skills_acquired']
        ) for exp in data['experience_details']]
        self.projects = [Project(**proj) for proj in data['projects']]
        self.achievements = [Achievement(**ach) for ach in data['achievements']]
        self.certifications = data['certifications']
        self.languages = [Language(**lang) for lang in data['languages']]
        self.interests = data['interests']

    def __str__(self):
        def format_dataclass(obj):
            return "\n".join(f"{field.name}: {getattr(obj, field.name)}" for field in obj.__dataclass_fields__.values())

        return (f"Personal Information:\n{format_dataclass(self.personal_information)}\n\n"
                "Education Details:\n" + "\n".join(
                    f"  - {edu.degree} in {edu.field_of_study} from {edu.university}, "
                    f"GPA: {edu.gpa}, Graduation Year: {edu.graduation_year}\n"
                    f"    Exams:\n" + "\n".join(f"      {exam.name}: {exam.grade}" for exam in edu.exam)
                    for edu in self.education_details
                ) + "\n\n"
                "Experience Details:\n" + "\n".join(
                    f"  - {exp.position} at {exp.company} ({exp.employment_period}), {exp.location}, {exp.industry}\n"
                    f"    Key Responsibilities:\n" + "\n".join(f"      - {resp.description}" for resp in exp.key_responsibilities) + "\n"
                    f"    Skills Acquired: {', '.join(exp.skills_acquired)}"
                    for exp in self.experience_details
                ) + "\n\n"
                "Projects:\n" + "\n".join(
                    f"  - {proj.name}: {proj.description}\n    Link: {proj.link}"
                    for proj in self.projects
                ) + "\n\n"
                "Achievements:\n" + "\n".join(
                    f"  - {ach.name}: {ach.description}"
                    for ach in self.achievements
                ) + "\n\n"
                "Certifications: " + ", ".join(self.certifications) + "\n\n"
                "Languages:\n" + "\n".join(
                    f"  - {lang.language} ({lang.proficiency})"
                    for lang in self.languages
                ) + "\n\n"
                "Interests: " + ", ".join(self.interests)
            )