from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models

# Register your models here.
admin.site.register(models.TokenModel),
admin.site.register(models.Categories),
admin.site.register(models.Products)

class CustomUserAdminModel(UserAdmin):
    # ordering = ('date_joined', 'is_superuser') 
    # search_fields = ('name', 'user_phone', 'viloyat') 
    # list_filter = ('name', 'user_phone', 'viloyat', 'tuman') 
    list_display = ('username', 'phone', 'is_superuser')
 
    fieldsets = (  
        (None, {'fields': ('username', 'phone', 'password', )}), 
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser', 'groups', 'user_permissions')}), 
        # ('Group Permissions', { 
        #     'classes': ('collapse',), 
        #     'fields': ('groups', 'user_permissions',) 
        # }) 
    ) 
 
    add_fieldsets = ( 
        (None, { 
            'classes': ('wide',), 
            'fields': ( 
                'username', 'phone', 'is_active', 'password1', 'password2',  
                'is_staff') 
        } 
         ), 
    ) 

admin.site.register(models.MyUser,CustomUserAdminModel)