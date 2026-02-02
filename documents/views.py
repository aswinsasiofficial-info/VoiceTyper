from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Document
from .export import export_txt, export_pdf, export_docx


def editor(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        Document.objects.create(title=title, content=content)
        return redirect("documents:dashboard")

    return render(request, "voice_editor.html")


def dashboard(request):
    docs = Document.objects.all().order_by("-created_at")
    return render(request, "document_dashboard.html", {"docs": docs})


def update_doc(request, id):
    doc = get_object_or_404(Document, id=id)

    if request.method == "POST":
        doc.title = request.POST.get("title")
        doc.content = request.POST.get("content")
        doc.save()
        return redirect("documents:dashboard")

    return render(request, "document_editor.html", {"doc": doc})


def delete_doc(request, id):
    doc = get_object_or_404(Document, id=id)
    doc.delete()
    return redirect("documents:dashboard")


def download(request, doc_id, filetype):
    doc = get_object_or_404(Document, id=doc_id)

    if filetype == "txt":
        return export_txt(doc.content, doc.title)
    elif filetype == "pdf":
        return export_pdf(doc.content, doc.title)
    elif filetype == "docx":
        return export_docx(doc.content, doc.title)



