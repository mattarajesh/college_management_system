from django.shortcuts import render,redirect
from .models import student

# Add this exact function block
def home(request):
    return render(request, 'students/home.html')
def student_dashboard(request):
    return render(request, "students/student_dashboard.html")
def add_student(request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        email = request.POST["email"]

        student.objects.create(
            name = name,
            age = age,
            email = email
        )
        return redirect("home")
    return render(request,"students/add_student.html")
def list_student(request):
    students = student.objects.all()

    context = {
        "students":students
    }
    return render(request,"students/list_student.html",context)
