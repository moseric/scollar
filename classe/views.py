from django.shortcuts import render
from django.shortcuts import redirect
from .models import classes
from django.http import HttpResponse, JsonResponse

# Create your views here.
def ajouter_classe(request):
    if request.method == "POST":
        nom = request.POST.get("nom")
        niveau = request.POST.get("niveau")

        classes.objects.create(
            nom=nom,
            enseignant=niveau
        )

    return HttpResponse("bdhhddgssbbsbs")