from django.shortcuts import render,redirect
from .models import emploies
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

# Create your views here.
def emploi(request):
    jours = request.POST.get('jours')
    debut = request.POST.get('heure_debut')
    fin = request.POST.get('heure_fin')
    heure = request.POST.get('nombre_heure')
    matiere = request.POST.get('matiere')
    enseignant = request.POST.get('enseignant')

    # enregsitrer les donner dans la base de donner
    emploie = emploies(
        jours = jours,
        heure_debut= debut,
        heure_fin = fin,
        matiere = matiere,
        nombre_heure = heure,
        enseignant = enseignant
    )
    emploie.save()
    messages.success(request,'Emploie du temps enregistrer avec succès')
    return redirect('dashboard')
