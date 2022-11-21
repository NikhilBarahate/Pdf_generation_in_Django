from django.shortcuts import redirect, render
from app1.models import Student
from app1.forms import StudentForm

from app1.utils import render_to_pdf, download_to_pdf


# Create your views here.
def student_View(request):
    form = StudentForm()
    template_name = 'app1/student.html'
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showstudent_url')

    context = {'form': form}
    return render(request, template_name, context)

def showstudent_View(request):
    data = Student.objects.all()
    template_name = 'app1/showstudent.html'
    context = {'data': data}
    return render(request, template_name, context)



def ResultList(request):
    template_name = "app1/pdf.html"
    records = Student.objects.all().order_by("rn")

    return render_to_pdf(
        template_name,
        {
            "record": records,
        },
    )

def DownloadList(request):
    template_name = "app1/pdf.html"
    records = Student.objects.all().order_by("rn")

    return download_to_pdf(
        template_name,
        {
            "record": records,
        },
    )

def specificRecord(request, id):
    template_name = "app1/specific.html"
    records = Student.objects.get(rn=id)

    return render_to_pdf(
        template_name,
        {
            "record": records,
        },
    )