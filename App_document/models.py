from django.db import models

# Create your models here.
class Document(models.Model):
        name    = models.CharField(verbose_name="Nom", max_length=200)
        file    = models.FileField(verbose_name="Fichier", upload_to="uploads")
        created_at    = models.DateTimeField(verbose_name="Date de création", auto_now_add=True)