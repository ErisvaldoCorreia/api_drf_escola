from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from exemplo_inicial.views import alunos, AlunoViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculasAlunos, ListaAlunosMatriculados


router = routers.DefaultRouter()
router.register('list_alunos', AlunoViewSet, basename='Alunos')
router.register('list_cursos', CursoViewSet, basename='Cursos')
router.register('list_matriculas', MatriculaViewSet, basename='Matriculas')

schema_view = get_schema_view(
   openapi.Info(
      title="Escola DRF API - Curso",
      default_version='v1',
      description="Documentação da API de escola criada em curso com Django Rest Framework",
      contact=openapi.Contact(email="devwebjunior@apidev.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
  
    # rota padrão inicial para acessar painel admin do django
    path('admin/', admin.site.urls),

    # rotas criada para resposta teste usando modelo view em response
    path('alunos/', alunos),
    
    # rota base para api e listagens controladas pelo rest framework
    path('api/', include(router.urls)),
    path('api/aluno/<int:pk>/matriculas/', ListaMatriculasAlunos.as_view()),
    path('api/curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),

    # rotas para documentação swagger
    path('api/doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
