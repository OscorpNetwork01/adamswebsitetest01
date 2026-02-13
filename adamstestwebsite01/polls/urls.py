from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),    #Va automatiquement activer la fonction views.detail pour display le bon ID
    path("<int:question_id>/results/", views.results, name="results"), 
    path("<question_id>/vote/", views.vote, name="vote"),
]