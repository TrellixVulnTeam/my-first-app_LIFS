from django.urls import path
from . import views #Importando todas as nossas views do aplicativo gradeHoraria

urlpatterns = [
    path('', views.grade_list, name='grade_list'),
	
]