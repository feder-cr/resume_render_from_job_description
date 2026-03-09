import re


def extract_contact_info(text):

    email = re.search(r"\S+@\S+", text)
    phone = re.search(r"\+?\d[\d\s\-]{8,}", text)

    name = text.split("\n")[0]

    return {
        "name": name,
        "email": email.group() if email else "",
        "phone": phone.group() if phone else ""
    }