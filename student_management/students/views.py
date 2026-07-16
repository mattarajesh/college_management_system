from django.shortcuts import render

# Add this exact function block
def home(request):
    return render(request, 'students/home.html')