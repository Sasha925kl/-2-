from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Resume, Profile, ResumeTemplate


class ResumeForm(forms.ModelForm):
    template = forms.ModelChoiceField(
        queryset=ResumeTemplate.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None,
        required=True,
        label="Оберіть шаблон"
    )

    class Meta:
        model = Resume
        fields = [
            'full_name',
            'email',
            'phone',
            'education',
            'experience',
            'skills',
            'photo',
            'template'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше ім’я'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@example.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+380 XXX XXX XXX'
            }),
            'education': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Освіта'
            }),
            'experience': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Досвід роботи'
            }),
            'skills': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Навички'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Логін")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']


class ResumeTemplateForm(forms.ModelForm):
    class Meta:
        model = ResumeTemplate
        fields = ["name", "html_file", "css_file", "preview_image"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'html_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'css_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'preview_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
