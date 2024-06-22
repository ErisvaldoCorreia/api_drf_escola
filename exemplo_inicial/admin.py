from django.contrib import admin
from exemplo_inicial.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
  list_display = (
    'id', 'nome', 'cpf', 'rg', 'data_nascimento'
  )
  list_display_links = ('id', 'nome')
  search_fields = ('nome',)
  list_per_page = 10

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
  list_display = (
    'id', 'codigo', 'descricao', 'nivel'
  )
  list_display_links = ('id', 'codigo')
  search_fields = ('nivel',)
  list_per_page = 10

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
  list_display = (
    'id', 'aluno', 'curso', 'periodo'
  )
  list_display_links = ('id',)
  list_per_page = 10

admin.site.register(Matricula, Matriculas)
