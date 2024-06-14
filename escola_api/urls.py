from django.contrib import admin
from django.urls import path, include

from exemplo_inicial.views import alunos, AlunoViewSet, CursoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('list_alunos', AlunoViewSet, basename='Alunos')
router.register('list_cursos', CursoViewSet, basename='Cursos')

urlpatterns = [
  
    # rota padrão inicial para acessar painel admin do django
    path('admin/', admin.site.urls),

    # rotas criada para resposta teste usando modelo view em response
    path('alunos/', alunos),
    
    # rota base para api e listagens controladas pelo rest framework
    path('api/', include(router.urls)),
]
