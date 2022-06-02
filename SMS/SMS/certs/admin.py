from django.contrib import admin

from .models import Certs

class CertsAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam_name', 'exam_type', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'exam_name')
    search_fields = ('exam_name', 'exam_type')


admin.site.register(Certs, CertsAdmin)


