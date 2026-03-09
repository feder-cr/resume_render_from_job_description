from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO


def generate_pdf(text):

    buffer = BytesIO()

    c = canvas.Canvas(buffer, pagesize=letter)

    y = 750

    for line in text.split("\n"):

        c.drawString(50, y, line[:90])

        y -= 15

        if y < 50:
            c.showPage()
            y = 750

    c.save()

    buffer.seek(0)

    return buffer