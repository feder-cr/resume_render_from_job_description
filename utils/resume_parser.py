import pdfplumber
import docx


def extract_text_from_pdf(file):

    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    return text


def extract_text_from_docx(file):

    doc = docx.Document(file)

    return "\n".join([p.text for p in doc.paragraphs])