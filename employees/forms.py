from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField
from .models import Employe

class RegisterForm(forms.ModelForm):
    # поля для создания User (не "встроенная регистрация", а своя форма)
    username = forms.CharField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Employe
        fields = [
            "phone", "birth_date", "passport_id", "address", "city",
            "education", "specialization", "experience_years",
            "desired_position", "desired_salary", "about"
        ]

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("password1") != cleaned.get("password2"):
            raise forms.ValidationError("Пароли не совпадают")
        return cleaned

    def save(self, commit=True):
        # создаём User + Applicant
        user = User.objects.create_user(
            username=self.cleaned_data["username"],
            password=self.cleaned_data["password1"]
        )
        applicant = super().save(commit=False)
        applicant.user = user
        if commit:
            applicant.save()
        return applicant


class LoginForm(AuthenticationForm):
    captcha = CaptchaField()   # ✅ Captcha Field
