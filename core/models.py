from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Documento(models.Model):
    titulo = models.CharField(max_length=400)
    arquivo = models.FileField(upload_to='documentos/')
    texto_extraido = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.titulo} ({self.arquivo.name})"
