from django.db import models
from django.contrib.auth.models import User


class ResumeTemplate(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва шаблону")
    html_file = models.FileField(
        upload_to='templates/html/',
        verbose_name="HTML файл"
    )
    css_file = models.FileField(
        upload_to='templates/css/',
        verbose_name="CSS файл"
    )
    preview_image = models.ImageField(
        upload_to='template_previews/',
        blank=True,
        null=True,
        verbose_name="Прев’ю шаблону"
    )

    def __str__(self):
        return self.name

class Resume(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    photo = models.ImageField(upload_to="resume_photos/", blank=True, null=True) 
    template = models.ForeignKey("ResumeTemplate", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    