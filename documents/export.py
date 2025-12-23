from django.http import HttpResponse
from reportlab.pdfgen import canvas
from docx import Document as DocxDocument


def export_txt(content, title):
    response = HttpResponse(content, content_type="text/plain")
    response["Content-Disposition"] = f'attachment; filename="{title}.txt"'
    return response


def export_pdf(content, title):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="{title}.pdf"'

    pdf = canvas.Canvas(response)
    y = 800
    for line in content.split("\n"):
        pdf.drawString(40, y, line)
        y -= 15
    pdf.save()

    return response


def export_docx(content, title):
    doc = DocxDocument()
    doc.add_paragraph(content)

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    response["Content-Disposition"] = f'attachment; filename="{title}.docx"'
    doc.save(response)

    return response
