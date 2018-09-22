from django.shortcuts import render

# Create your views here.
def grade_list(request):
    return render(request, 'gradeHoraria/grade_list.html', {})