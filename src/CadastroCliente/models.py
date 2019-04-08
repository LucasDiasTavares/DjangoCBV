from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=50, null=True, blank=False)
    email = models.CharField(max_length=50, null=True, blank=True)
    endereco = models.CharField(max_length=50, null=True, blank=True)
    telefone = models.IntegerField(null=True, blank=False)
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome + ' - ' + str(self.telefone)
