from django.db import models

# Create your models here.
class matieres(models.Model):
    nom = models.TextField(max_length=150, null = True)
    coefficient = models.IntegerField( null = True)
    def __str__(self):
        return self.nom