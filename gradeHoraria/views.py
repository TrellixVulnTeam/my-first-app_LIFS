from django.shortcuts import render
from django.utils import timezone
from .models import Grade

# Create your views here.
def grade_list(request):
    grades = Grade.objects.filter(published_date__lte=timezone.now()).order_by('title') 
    return render(request, 'gradeHoraria/grade_list.html', {'grades': grades})
