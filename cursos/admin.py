from django.contrib import admin
from .models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

admin.site.register(Curso, CursoAdmin)
