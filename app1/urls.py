from django.urls import path
from app1.views import student_View, showstudent_View, ResultList, DownloadList, specificRecord

urlpatterns = [
    path('sv/', student_View, name="student_url"),
    path('ss/', showstudent_View, name="showstudent_url"),
    path("list/", ResultList, name="list"),
    path("download/", DownloadList, name="download"),
    path('sp/<int:id>/', specificRecord, name="specific_url"),
]