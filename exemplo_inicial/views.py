#from django.shortcuts import render

# Create your views here.
# -- acima código base criado pelo django para retornar views renderizadas

from django.http import JsonResponse

def alunos(request):
  if request.method == 'GET':
    """Retornando dados da lista usando Django puro"""
    alunos = list(Aluno.objects.values())
    return JsonResponse(alunos, safe=False)
  

# --- Aplicando modelo django rest framework ---

from rest_framework import viewsets
from exemplo_inicial.models import Aluno, Curso
from exemplo_inicial.serializer import AlunoSerializer, CursoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
  """Exibindo todos os alunos cadastrados"""
  queryset = Aluno.objects.all()
  serializer_class = AlunoSerializer

class CursoViewSet(viewsets.ModelViewSet):
  """Exibindo todos os alunos cadastrados"""
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer

