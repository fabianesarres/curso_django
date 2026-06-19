from django.db import models

# Create your models here.
# aqui vou criar minhas classes de entidade


class Autor(models.Model):
# atributo
# o atributo id é automático
# chave primária: imútavel, universal e única
    nome = models.CharField(max_length=100)
    biografia = models.TextField(blank = True)
    email = models.EmailField()
#definir uma função = usar 'DEF':
    def __str__(self):
        return self.nome
    class Meta:
        db_table = 'autor'
    
#--------------------------------------------------------------------------------#    
#Nova classe criada na 3a aula - 12/02/26 - class: EixoTecnologia
class EixoTecnologia(models.Model):
    nome = models.CharField(max_length=100)
#definir uma função = usar 'DEF':
    def __str__(self):
        return self.nome
    class Meta:
       db_table = 'eixo'


class chatbot(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self) -> str:
        return super().__str__()