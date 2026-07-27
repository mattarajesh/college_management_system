from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("students/", views.student_dashboard, name="student_dashboard"),
    path("add/", views.add_student, name="add_student"),
    path("student_list/", views.list_student, name="student_list"),
    path("update/",views.update_student,name="update_student"),
]