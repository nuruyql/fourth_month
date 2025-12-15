from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm
from .models import Employe

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "employees/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("applicants")
    else:
        form = LoginForm(request)
    return render(request, "employees/login.html", {"form": form})


@login_required
def applicants_view(request):
    people = Employe.objects.select_related("user").order_by("-created_at")
    return render(request, "employees/empl_list.html", {"people": people})


@login_required
def applicant_detail_view(request, id):
    person = get_object_or_404(Employe, id=id)
    return render(request, "employees/empl_detail.html", {"person": person})