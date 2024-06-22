from django.db import models

class Aluno(models.Model):
  nome = models.CharField(max_length=30)
  cpf = models.CharField(max_length=11)
  rg = models.CharField(max_length=9)
  data_nascimento = models.DateField()

  def __str__(self):
    return self.nome


class Curso(models.Model):
  NIVEL = (
    ('B', 'Basico'),
    ('I', 'Intermediario'),
    ('A', 'Avancado')
  )

  codigo = models.CharField(max_length=10)
  descricao = models.CharField(max_length=100)
  nivel = models.CharField(
    max_length=1, blank=False, null=False, default='B', choices=NIVEL
  )

  def __str__(self):
    return self.codigo
  

class Matricula(models.Model):
  PERIODO = (
    ('M', 'Matutino'),
    ('V', 'Vespertino'),
    ('N', 'Noturno')
  )

  aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
  curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
  periodo = models.CharField(
    max_length=1, blank=False, null=False, default='M', choices=PERIODO
  )
