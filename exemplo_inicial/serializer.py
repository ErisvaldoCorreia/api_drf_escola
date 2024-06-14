from rest_framework import serializers
from exemplo_inicial.models import Aluno, Curso

class AlunoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Aluno
    fields = '__all__'
    # caso queira determinar conjuntos de campos especificos, 
    # podemos usar uma lista de campos direcionadas: 
    # fields = ['id', 'nome', 'cpf']

class CursoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Curso
    fields = '__all__'
    # caso queira determinar conjuntos de campos especificos, 
    # podemos usar uma lista de campos direcionadas: 
    # fields = ['id', 'nome', 'cpf']

