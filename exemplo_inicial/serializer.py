from rest_framework import serializers
from exemplo_inicial.models import Aluno, Curso, Matricula

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

class MatriculaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Matricula
    exclude = []
    # usando o exclude podemos dizer qual campo não gostariamos
    # de ver serializado. Deixar vazio, traz todos os campos!

class ListaMatriculaPorAlunoSerializer(serializers.ModelSerializer):
  curso = serializers.ReadOnlyField(source='curso.descricao')
  periodo = serializers.SerializerMethodField()
  class Meta:
    model = Matricula
    fields = ['curso', 'periodo']
  def get_periodo(self, obj):
    return obj.get_periodo_display()

    
class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
  aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
  class Meta:
    model = Matricula
    fields = ['aluno_nome']

