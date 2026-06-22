from django.db import models

# Create your models here.
class matieres(models.Model):
    nom = models.TextField(max_length=150, unique=True)
    coefficient = models.IntegerField()
    def __str__(self):
        return self.nom