from django.contrib import admin

# Register your models here.
from django.contrib import admin, messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

def approve_users(modeladmin, request, queryset):
    uploader_group, _ = Group.objects.get_or_create(name='Uploader')
    pending_group = Group.objects.filter(name='Pending').first()
    count = 0
    for user in queryset:
        user.is_active = True
        user.save()
        user.groups.add(uploader_group)
        if pending_group:
            user.groups.remove(pending_group)
        count += 1
    messages.success(request, f"{count} usuário(s) aprovados e movidos para Uploader.")
approve_users.short_description = "Aprovar usuários e torná-los Uploader"

class CustomUserAdmin(DjangoUserAdmin):
    actions = DjangoUserAdmin.actions + (approve_users,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
