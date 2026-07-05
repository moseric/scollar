from django.shortcuts import render,redirect
from .models import matieres
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
# Create your views here.
def ajouter_classe(request):
    if request.method == 'POST':
        nom = request.POST.get('matiere')
        coefficient = request.POST.get('coefficient')
        matiere = matieres(nom = nom, coefficient = coefficient)
        matiere.save()
        messages.success(request, 'Matière ajoutée avec succès.')
        return redirect('dashboard')
    else:
        matieres_list = matieres.objects.all()
        messages.success(request, 'erreur de lors de l\'ajout de la matière.')
        return redirect('dashbord')