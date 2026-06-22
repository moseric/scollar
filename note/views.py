from django.shortcuts import render
from django.http import HttpResponse
from .models import notes

# Create your views here.
def notes(request):
    eleve = [
        {
            "nom": "Doe",
            "prenom": "John",
            "int1": 3,
            "int2": None,
            "int3": 2,
            "int4": 3,
            "moy_int": 3,
            "devoir": 4,
            "compo": 3,
            "moy_trim": 3.5,
            "rang": 1,
            "observation": "Excellent"
        },
        {
            "nom": "bgh",
            "prenom": "ghytr",
            "int1": None,
            "int2": None,
            "int3": None,
            "int4": None,
            "moy_int": None,
            "devoir": None,
            "compo": None,
            "moy_trim": None,
            "rang": None,
            "observation": None
        }
    ]
    return render(request, 'note.html', {'eleve': eleve})