from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from datetime import datetime
from .models import personnel


# la fonction qui permettant d'enregistrer les personnes
def personna(request):
    if request.method == "POST":
        nom = request.POST.get('name')
        prenom = request.POST.get('prenom')
        sexe = request.POST.get('sexe')
        date_naissance = request.POST.get('date_naissance')
        post = request.POST.get('poste')
        num_educmaster = request.POST.get('num_educmaster')
        statut = request.POST.get('diplome')
        whatsapp = request.POST.get('whatsapp')
        classe = request.POST.getlist('classe')
        identifiant = nom[:2]+prenom[:2]+whatsapp[6:]
        
        pers = personnel(
            nom = nom,
            prenom = prenom,
            sexe = sexe,
            date_naissance = date_naissance,
            identifiant = identifiant,
            poste = post,
            num_educmaster = num_educmaster,
            statut = statut,
            whatsapp = whatsapp,
            classes = classe
            
        )
        pers.save()
        # verifiction du contenue de la classe avant son insertion
    
        return redirect('register',id=2)
        