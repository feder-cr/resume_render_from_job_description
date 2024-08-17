# Resume_Builder_AIHawk

🚀 **Join Our Telegram Community!** 🚀

Join our **Telegram community** for:
- **Support with AIHawk software**
- **Share your experiences** with AIhawk and learn from others
- **Job search tips** and **resume advice**
- **Idea exchange** and resources for your projects

📲 **[Join now!](https://t.me/AIhawkCommunity)**


## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [Dependencies](#Dependencies)
7. [Documentation](#documentation)
8. [Troubleshooting](#troubleshooting)
9. [Conclusion](#conclusion)
10. [How to Contribute](#how-to-contribute)
   - [Web Designers](#web-designers)
   - [Prompt Engineers](#prompt-engineers)
   - [Software Engineers](#software-engineers)
   - [Other Contributions](#other-contributions)
11. [Credits](#credits)
12. [License](#license)
13. [Disclaimer](#disclaimer)


## Introduction

Resume_Builder_AIHawk is powerful Python tool that simplifies the creation of visually stunning resumes quickly and easily. With this tool, you can not only build a resume from scratch but also tailor it perfectly based on a specific job description. By inputting the URL of the job listing, Resume_Builder_AIHawk customizes your resume to match the exact requirements and skills needed, making it ideal for enhancing your chances of landing the job.


## Features

- **Interactive Command-Line Interface:** Navigate through options and prompts using a user-friendly CLI.
- **Dynamic Style Management:** Choose from a variety of pre-defined resume styles.
- **Job Description Integration:** Automatically tailor your resume based on a job URL.

## Installation

To get started with Resume_Builder_AIHawk, follow these steps:

1. **Download and Install Python:**

   Ensure you have the last Python version installed. If not, download and install it from Python's official website. For detailed instructions, refer to the tutorials:

   - [How to Install Python on Windows](https://www.geeksforgeeks.org/how-to-install-python-on-windows/)
   - [How to Install Python on Linux](https://www.geeksforgeeks.org/how-to-install-python-on-linux/)
   - [How to Download and Install Python on macOS](https://www.geeksforgeeks.org/how-to-download-and-install-python-latest-version-on-macos-mac-os-x/)

2. **Download and Install Google Chrome:**
   - Download and install the latest version of Google Chrome in its default location from the [official website](https://www.google.com/chrome).

3. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/resume_builder_AIHawk.git
    ```

4. **Navigate to the Project Directory:**

    ```bash
    cd resume_builder_AIHawk
    ```
5. **Install Dependencies:**

    Ensure you have `pip` installed, then run:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

### 1. Configuring `plain_text_resume.yaml`

The `plain_text_resume.yaml` file is crucial as it contains all your personal details and resume content. Follow these steps to configure it properly:

#### 1. Create the File

Create a file named `plain_text_resume.yaml` in the root directory of your project. This file will store all the necessary details to generate your resume.

#### 2. Define Personal Information

Fill in your personal information. This section includes your basic details and contact information:

```yaml
personal_information:
  name: [Name]
  surname: [Surname]
  date_of_birth: "[DD/MM/YYYY]"
  country: [Country]
  city: [City]
  address: [Address]
  phone_prefix: "[+Country Code]"
  phone: "[Phone Number]"
  email: [Email Address]
  github: [GitHub URL]
  linkedin: [LinkedIn URL]
```

- **name**: Your first name.
- **surname**: Your last name.
- **date_of_birth**: Your date of birth in the format `DD/MM/YYYY`.
- **country**: The country where you live.
- **city**: The city where you live.
- **address**: Your home address.
- **phone_prefix**: Your phone number prefix, e.g., `+1` for the USA.
- **phone**: Your phone number.
- **email**: Your email address.
- **github**: Your GitHub profile URL (optional).
- **linkedin**: Your LinkedIn profile URL (optional).

#### 3. Provide Education Details

List your educational qualifications. You can add multiple degrees:

```yaml
education_details:
  - degree: [Degree Type]
    university: [University Name]
    gpa: "[GPA]"
    graduation_year: "[Graduation Year]"
    field_of_study: [Field of Study]
    exam:
      [Course Name]: "[Grade]"
      [Course Name]: "[Grade]"
      [Course Name]: "[Grade]"
  - degree: [Degree Type]
    university: [University Name]
    gpa: "[GPA]"
    graduation_year: "[Graduation Year]"
    field_of_study: [Field of Study]
    exam:
      [Course Name]: "[Grade]"
      [Course Name]: "[Grade]"
      [Course Name]: "[Grade]"
```

- **degree**: Type of degree (e.g., BSc, MSc, PhD).
- **university**: Name of the university or institution.
- **gpa**: Your GPA (optional).
- **graduation_year**: The year you graduated.
- **field_of_study**: Your field of study (e.g., Computer Science).
- **exam**: List of courses and grades received. Add or remove entries as needed.

#### 4. List Experience Details

Provide information about your work experience. You can include multiple jobs:

```yaml
experience_details:
  - position: [Job Title]
    company: [Company Name]
    employment_period: "[MM/YYYY - MM/YYYY or Present]"
    location: [Location]
    industry: [Industry]
    key_responsibilities:
      - [Responsibility Description]
      - [Responsibility Description]
      - [Responsibility Description]
    skills_acquired:
      - [Skill]
      - [Skill]
      - [Skill]
  - position: [Job Title]
    company: [Company Name]
    employment_period: "[MM/YYYY - MM/YYYY or Present]"
    location: [Location]
    industry: [Industry]
    key_responsibilities:
      - [Responsibility Description]
      - [Responsibility Description]
      - [Responsibility Description]
    skills_acquired:
      - [Skill]
      - [Skill]
      - [Skill]
```

- **position**: Your job title.
- **company**: Name of the company where you worked.
- **employment_period**: The period you worked there (e.g., `01/2020 - 12/2021` or `Present`).
- **location**: City and country of the company's location.
- **industry**: The industry of the company.
- **key_responsibilities**: List of key responsibilities in bullet points.
- **skills_acquired**: List of skills acquired during this role.

#### 5. Detail Your Projects

Include projects that you have worked on:

```yaml
projects:
  - name: [Project Name]
    description: [Project Description]
    link: "[Project URL]"
  - name: [Project Name]
    description: [Project Description]
    link: "[Project URL]"
  - name: [Project Name]
    description: [Project Description]
    link: "[Project URL]"
```

- **name**: Name of the project.
- **description**: A brief description of the project.
- **link**: URL to the project or related resource (optional).

#### 6. Add Achievements

List notable achievements:

```yaml
achievements:
  - name: [Achievement Title]
    description: [Achievement Description]
  - name: [Achievement Title]
    description: [Achievement Description]
  - name: [Achievement Title]
    description: [Achievement Description]
  - name: [Achievement Title]
    description: [Achievement Description]
```

- **name**: Title of the achievement.
- **description**: Description of the achievement.

#### 7. List Certifications

Include any certifications you hold:

```yaml
certifications:
  - [Certification Name]
```

- **certification**: Name of the certification.

#### 8. Detail Your Language Skills

List the languages you speak and your proficiency levels:

```yaml
languages:
  - language: [Language]
    proficiency: [Proficiency Level]
  - language: [Language]
    proficiency: [Proficiency Level]
  - language: [Language]
    proficiency: [Proficiency Level]
```

- **language**: Name of the language.
- **proficiency**: Your proficiency level (e.g., Basic, Intermediate, Advanced).

#### 9. Add Interests

Include your personal interests:

```yaml
interests:
  - [Interest]
  - [Interest]
  - [Interest]
```

- **interest**: List your interests or hobbies.

#### Example `plain_text_resume.yaml`

An example `plain_text_resume.yaml` file is provided in the repository to guide you. Copy and modify it according to your personal details.

### 2. Configuring `secrets.yaml`

This file contains sensitive information. Never share or commit this file to version control.

- `openai_api_key: [Your OpenAI API key]`
  - Replace with your OpenAI API key for GPT integration
  - To obtain an API key, follow the tutorial at: https://medium.com/@lorenzozar/how-to-get-your-own-openai-api-key-f4d44e60c327
  - Note: You need to add credit to your OpenAI account to use the API. You can add credit by visiting the [OpenAI billing dashboard](https://platform.openai.com/account/billing).


## Usage

To run Resume_Builder_AIHawk, execute the following command from your terminal:

```bash
python main.py
```

## Dependencies

- Resume_Builder_AIHawk depends on the [lib_resume_builder_AIHawk repository](https://github.com/feder-cr/lib_resume_builder_AIHawk) repository. The library is automatically installed at program launch.

## Documentation

 todo

## Troubleshooting

If you encounter any issues, you can open an issue on GitHub. I'll be more than happy to assist you!

For immediate support and to connect with the AIHawk community, join our Telegram group.
📲 [Join now!](https://t.me/AIhawkCommunity)

## Conclusion

Resume_Builder_AIHawk simplifies the resume creation process by providing a flexible, style-driven approach. By configuring `plain_text_resume.yaml` and using the interactive prompts, you can easily generate professional resumes tailored to your needs.

## Contributors

- [feder-cr](https://github.com/feder-cr) - Creator and Lead Developer

## How to contribute

We welcome contributions from the community! Whether you are a designer, prompt engineer, software engineer, or have other skills to offer, there are several ways you can contribute to Resume_Builder_AIHawk:

### Web Designers

Help us enhance the visual appeal of our resume templates by creating custom CSS styles. Your unique design can become part of our project!

To learn how to contribute and add your design, [follow the guidelines for designers](https://github.com/feder-cr/lib_resume_builder_AIHawk/blob/main/how_to_contribute/web_designer.md).


### Prompt Engineers
Assist in refining and developing effective prompts for resume customization. [Learn how to contribute as a prompt engineer.](how_to_contribute/prompt_engineer.md)

### Software Engineers
Contribute by submitting pull requests to improve the codebase, fix bugs, or add new features. [Learn how to contribute as a software engineer.](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project)

### Other Contributions
You can also contribute by:
- Reporting issues
- Suggesting features
- Improving documentation

### Other Contributions
You can also contribute by:
- Reporting issues
- Suggesting features
- Improving documentation

For immediate support and to connect with the AIHawk community, join our Telegram group.
📲 [Join now!](https://t.me/AIhawkCommunity)


## Credits

    todo

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

The information provided by Resume_Builder_AIHawk is for general informational purposes only. The project is intended to assist with resume creation and may not cover all specific requirements for every job application.
