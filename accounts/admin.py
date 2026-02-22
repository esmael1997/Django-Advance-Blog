from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ("email", "is_staff", "is_active",)
    search_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        ('Authentication', {
            "fields": (
                "email", "password"
                ),
            }),
            ("Permissions", {
                "fields": (
                    "is_staff", "is_active"
                    ),
            }),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active")}
        ),
    )
    
    
admin.site.register(User, CustomUserAdmin)
    
    


