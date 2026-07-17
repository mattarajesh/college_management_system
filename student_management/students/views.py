from django.shortcuts import render,redirect
from .models import student

# Add this exact function block
def home(request):
    return render(request, 'students/home.html')
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
