#from django.shortcuts import render

# Create your views here.
# -- acima código base criado pelo django para retornar views

from django.http import JsonResponse

def alunos(request):
  if request.method == 'GET':
    alunos = { 'id': 1, 'name': 'Junior' }
    return JsonResponse(alunos)
  
