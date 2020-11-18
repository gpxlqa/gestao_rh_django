from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionario

class Documentos(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True)
    arquivo = models.FileField(upload_to='documentos')

    def get_absolute_url(self):
        return reverse('list_funcionarios', args=[self.pertence.id])

    def __str__(self):
        return self.descricao

