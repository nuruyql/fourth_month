from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.register_view, name="registerr"),
    path("login/", views.login_view, name="login"),
    path("applicants/", views.applicants_view, name="applicants"),
    path("applicants/<int:id>/", views.applicant_detail_view, name="applicant_detail"),
]