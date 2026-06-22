from django.db import models

# Create your models here.
class emploies(models.Model):
    jours = models.CharField(max_length=20)
    heure_debut = models.CharField()
    heure_fin = models.CharField()
    matiere = models.TextField(max_length=150,null=True)
    nombre_heure = models.CharField(max_length=50,null=True)
    enseignant = models.CharField(max_length=100)
    def __str__(self):
        return self.matiere