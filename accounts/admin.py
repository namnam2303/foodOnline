from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'is_admin', 'is_staff', 'is_active', 'is_superadmin', 'created_date')
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'username')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active', 'is_superadmin')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'username', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('created_date',)
    filter_horizontal = ()

# Register the new UserAdmin
admin.site.register(User, CustomUserAdmin)

# Register the UserProfile model
admin.site.register(UserProfile)