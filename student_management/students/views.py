from django.shortcuts import render, redirect
from django.contrib import messages
from .models import student
from django.core.paginator import Paginator

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
    name=name,
    age=age,
    email=email
    )
        messages.success(request, "Student added successfully!")
        return redirect("student_list")
    return render(request,"students/add_student.html")
def list_student(request):

    students = student.objects.all()

    paginator = Paginator(students, 5)   # Show 5 students per page

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj
    }

    return render(request, "students/list_student.html", context)
def update_student(request, id):

    s = student.objects.get(id=id)

    if request.method == "POST":

        s.name = request.POST["name"]
        s.age = request.POST["age"]
        s.email = request.POST["email"]

        s.save()
        messages.success(request, "Student updated successfully!")
        return redirect("student_list")

    context = {
        "student": s
    }

    return render(request, "students/update_student.html", context)
def delete_student(request, id):

    s = student.objects.get(id=id)

    if request.method == "POST":

        s.delete()
        messages.success(request, "Student deleted successfully!")
        return redirect("student_list")

    context = {
        "student": s
    }

    return render(request, "students/delete_student.html", context)

def view_student(request, id):

    s = student.objects.get(id=id)

    context = {
        "student": s
    }

    return render(request, "students/view_student.html", context)


def search_student(request):

    students = None

    if request.method == "POST":

        name = request.POST["name"]

        students = student.objects.filter(name__icontains=name)

    context = {
        "students": students
    }

    return render(request, "students/search_student.html", context)