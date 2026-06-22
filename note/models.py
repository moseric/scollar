from django.db import models

# Create your models here.
class notes(models.Model):
    eleve = models.CharField(max_length=100)
    matiere = models.CharField(max_length=150)
    niveau = models.CharField(max_length=50)
    int1 = models.DecimalField(max_digits=4, decimal_places=2, null=True,blank=True)
    int2 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    int3 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    int4 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    moy_int = models.DecimalField(max_digits=4, decimal_places=2,null=True, blank=True)
    devoir = models.DecimalField(max_digits=4, decimal_places=2,null=True, blank=True)
    compo = models.DecimalField(max_digits=4, decimal_places=2,null=True, blank=True)
    moyen_trim = models.DecimalField(max_digits=4, decimal_places=2,null=True, blank=True)
    trimestre = models.CharField(max_length=40,null=True, blank=True)

    def __str__(self):
        return f"{self.eleve} - {self.matiere}: {self.moyen_trim}"