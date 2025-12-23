from django.urls import path
from . import views

app_name = "documents"

urlpatterns = [
    path("", views.editor, name="editor"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("update/<int:id>/", views.update_doc, name="update"),
    path("delete/<int:id>/", views.delete_doc, name="delete"),
    path("download/<int:doc_id>/<str:filetype>/", views.download, name="download"),
]
