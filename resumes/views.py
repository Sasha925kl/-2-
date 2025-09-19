from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseForbidden
from .models import ResumeTemplate, Resume, Profile
from .forms import ResumeForm, RegisterForm, LoginForm, UserUpdateForm, ProfileUpdateForm, ResumeTemplateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def resume_create(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES) 
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user  
            resume.save()
            return redirect('resume_list')
    else:
        form = ResumeForm()
    return render(request, 'resumes/resume_create.html', {'form': form})


def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'resumes/resume_list.html', {'resumes': resumes})

def resume_detail(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    resumes = Resume.objects.all().order_by("id")
    return render(request, "resumes/resume_detail.html", {
        "resume": resume,
        "resumes": resumes
    })
def resume_delete(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    if not (request.user.is_superuser or request.user == resume.user):
        return HttpResponseForbidden("Ви не маєте доступу для видалення цього резюме.")
    resume.delete()
    messages.success(request, "Резюме успішно видалено!")
    return redirect('resume_list')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request): 
    logout(request)
    return redirect("home")


def profile(request):
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)

def is_admin(user):
    return user.is_staff

def resume_edit(request, pk):
    resume = get_object_or_404(Resume, pk=pk)


    if not (request.user.is_superuser or request.user == resume.user):
        return HttpResponseForbidden("Ви не маєте доступу для редагування цього резюме.")

    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('resume_detail', pk=resume.pk)
    else:
        form = ResumeForm(instance=resume)

    return render(request, 'resumes/resume_edit.html', {'form': form, 'resume': resume})

def templates_list(request):
    templates = ResumeTemplate.objects.all()

    if request.method == "POST":
        form = ResumeTemplateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("templates_list")
    else:
        form = ResumeTemplateForm()

    return render(request, "templates/templates_list.html", {
        "templates": templates,
        "form": form
    })