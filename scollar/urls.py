"""
URL configuration for scollar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from eleves import views
from note import views as note_views
from personnel import views as personnel_views
from classe import views as classe_views
from emploie import views as emploi_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eleves/', views.index),
    path('', views.home, name='home'),
    path('register/<int:id>/', views.register, name='register'),
    path('register_eleve/', views.register_eleve, name='register_eleve'),
    path('notes/', note_views.notes, name='notes'),
    path('dashboard/',views.compter, name='dashboard'),
    path('dashboard/saisi_note/',views.saisie, name="saisi_note"),
    path('personna/',personnel_views.personna, name='personna'),
    path('ajouter-classe/', classe_views.ajouter_classe, name='ajouter_classe'),
    path('ajouter_emploie', emploi_views.emploi, name='ajouter_emploie')
]
