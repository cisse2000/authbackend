from django.contrib import admin
# from App.models import User

from django.contrib.auth import get_user_model
User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name','last_name','email']
    ordering = ['id']
 
admin.site.register(User, UserAdmin)


