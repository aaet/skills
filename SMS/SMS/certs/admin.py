from django.contrib import admin

from .models import Certs, Users


class CertsAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam_name', 'exam_type', 'created_at', 'updated_at', 'is_published', 'user')
    list_display_links = ('id', 'exam_name')
    search_fields = ('exam_name', 'exam_type')
    list_editable = ('is_published',)
    list_filter = ('user', 'is_published')


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'staff', 'division', 'gender', 'birthday')
    list_display_links = ('user',)
    search_fields = ('user', 'division')


admin.site.register(Certs, CertsAdmin)
admin.site.register(Users, UsersAdmin)


