from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from enquetes.models import Enquete

def welcome(request):
    template = loader.get_template('welcome.html')
    return HttpResponse(template.render({}, request))

def exibir_enquete(request, enquete_id):
    enquete = Enquete.objects.get(id=enquete_id)
    context = {'enquete':enquete}
    return render(request,'enquete.html',context)