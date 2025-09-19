from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'email', 'phone', 'created_at')
    search_fields = ('full_name', 'email', 'phone', 'user__username')

    def get_queryset(self, request):
        return super().get_queryset(request)

    def has_change_permission(self, request, obj=None):
        if obj is None: 
            return True
        return request.user.is_superuser or obj.user == request.user


    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or obj.user == request.user