from rest_framework import serializers
from exemplo_inicial.models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Aluno
    fields = '__all__'
    # caso queira determinar conjuntos de campos especificos, 
    # podemos usar uma lista de campos direcionadas: 
    # fields = ['id', 'nome', 'cpf']

