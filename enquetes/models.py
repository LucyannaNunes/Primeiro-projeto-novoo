import datetime
from django.db import models
from django.utils import timezone

class Perguntas(models.Model):
    texto_pergunta = models.CharField(max_length=200)
    data_publicado = models.DateTimeField("date published")

    def __str__(self):
        return self.texto_pergunta
    
    def foi_publicado_recetemente(self):
        return self.data_publicado >= timezone.now() - datetime.timedelta(days=1)
 

class Escolha(models.Model):
    pergunta = models.ForeignKey(Perguntas, on_delete = models.CASCADE)
    texto_escolha = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto_escolha
    

