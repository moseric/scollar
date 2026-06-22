from django.db import models

# Create your models here.
class classes(models.Model):
    nom = models.TextField(max_length=150, unique=True)
    enseignant = models.CharField(max_length=100)
    note = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return self.nom