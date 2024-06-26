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

from rest_framework import viewsets, generics
from exemplo_inicial.models import Aluno, Curso, Matricula
from exemplo_inicial.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaPorAlunoSerializer, ListaAlunosMatriculadosSerializer

class AlunoViewSet(viewsets.ModelViewSet):
  """Exibindo todos os alunos cadastrados"""
  queryset = Aluno.objects.all()
  serializer_class = AlunoSerializer

class CursoViewSet(viewsets.ModelViewSet):
  """Exibindo todos os alunos cadastrados"""
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
  """Exibindo todos as matriculas registradas"""
  queryset = Matricula.objects.all()
  serializer_class = MatriculaSerializer

class ListaMatriculasAlunos(generics.ListAPIView):
  """Exibindo as matriculas de cada aluno"""
  def get_queryset(self):
    queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
    return queryset
  serializer_class = ListaMatriculaPorAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
  """Exibindo os alunos matriculados em um curso"""
  def get_queryset(self):
    queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
    return queryset
  serializer_class = ListaAlunosMatriculadosSerializer

