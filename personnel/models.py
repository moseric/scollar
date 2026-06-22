from django.db import models

# Modèle pour les classes/niveaux
class Classe(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    
    class Meta:
        ordering = ['nom']
    
    def __str__(self):
        return self.nom

# Modèle pour le personnel
class personnel(models.Model):
    POSTE_CHOICES = [
        ('Professeur', 'Professeur'),
        ('Directeur', 'Directeur'),
        ('Assistant', 'Assistant'),
        ('Administratif', 'Administratif'),
        ('Autre', 'Autre'),
    ]
    
    STATUT_CHOICES = [
        ('Actif', 'Actif'),
        ('Inactif', 'Inactif'),
    ]
    
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=10)
    date_naissance = models.DateField()
    identifiant = models.CharField( max_length=50)
    poste = models.CharField(max_length=50, choices=POSTE_CHOICES, default='Professeur')
    num_educmaster = models.CharField(max_length=20)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='Actif')
    whatsapp = models.CharField(max_length=20)
    classes = models.JSONField(null=True)
    date_ajout = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['nom', 'prenom']

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    