from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from eleves.models import eleves
from django.db import IntegrityError
from personnel.models import personnel
from django.db.models import Count,Q
from emploie.models import emploies

# Create your views here.
def index(request):
    return render(request, 'dashboard.html')
def home(request):
    return render(request, 'login.html')

# Afficher le formulaire d'enregistrement d'un élève et de personnel
def register(request,id):
    return render(request, 'register.html',{'id':id})

# afficher la page admin
def dash(request):
    return render(request ,'dashboard.html')

#affiche note de saisie
def saisie(request):
    return render(request,'saisi_note.html')

# Traiter l'enregistrement d'un élève
@require_http_methods(["POST"])
def register_eleve(request):
    try:
        if request.method=="POST":
            # Récupérer les données du formulaire
            nom_prenom = request.POST.get('nom_prenom')
            sexe = request.POST.get('sexe')
            date_naissance = request.POST.get('date_naissance')
            niveau = request.POST.get('niveau')
            num_educmaster = request.POST.get('num_educmaster')
            statut = request.POST.get('statut')
            whatsapp = request.POST.get('whatsapp')
            
            # Créer et sauvegarder l'élève
            eleve = eleves(
                nom_prenom=nom_prenom, 
                sexe=sexe,
                date_naissance=date_naissance,
                niveau=niveau,
                num_educmaster=num_educmaster,
                statut=statut,
                whatsapp=whatsapp
            )
            eleve.save()
            
            return redirect('register',id=3)
    except IntegrityError:
        return redirect('register',id=4)

# compter les eleves
def compter(request):
    try:
        nombre=eleves.objects.values('nom_prenom').count()
        nom=eleves.objects.values('niveau').distinct().count()
        person=personnel.objects.values('identifiant').count()
        infos = eleves.objects.all().order_by('niveau')
        effectifs = eleves.objects.values('niveau').annotate(effectif=Count('id'),fille=Count('id',filter=Q(sexe='Masculin')),garcon=Count('id',filter=Q(sexe='Feminin'))).order_by('-niveau')
        emploie = emploies.objects.all().order_by('jours')
        return render(request,'dashboard.html',{'nombre':nombre,'nom':nom,'person':person,'effectifs':effectifs,'infos':infos,'emploie':emploie})
    except IntegrityError:
        return HttpResponse('erreur de mise a jurs des donner')

# affichage de la partie admine des parents
def admin1(request):
    return render(request,'dashbord_enseignant.html')
def admin2(request):
    return render(request,'admin_enseigant.html')