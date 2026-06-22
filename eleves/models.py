from django.db import models

class eleves(models.Model):
    # Create your models here.
    nom_prenom= models.CharField(max_length=100)
    sexe =models.CharField(max_length=10)
    date_naissance = models.DateField()
    niveau = models.CharField(max_length=50)
    num_educmaster = models.CharField(max_length=20,unique=True)
    statut = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nom_prenom} "