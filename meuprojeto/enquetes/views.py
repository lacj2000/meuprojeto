from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def welcome(request):
    template = loader.get_template('welcome.html')
    return HttpResponse(template.render({}, request))

def student(request):
    context = {
        'student': 'luiz junior',
    }
    return render(request, 'student/index.html', context)