from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from enquetes.models import Enquete

def welcome(request):
    template = loader.get_template('welcome.html')
    return HttpResponse(template.render({}, request))

def exibir_enquete(request, enquete_id):
    enquete = Enquete()
    if enquete_id == 1:
        enquete = Enquete(enquete_id,"Por que o céu é azul?","26/10/1989")
    if enquete_id == 2:
        enquete = Enquete(enquete_id,"Tem sempre alguma coisa por dizer","23/07/1989")
    if enquete_id == 3:
        enquete = Enquete(enquete_id,"Como o velho jonh dizia, a vida é um cabaré?","02/12/2013")
    context = {'enquete':enquete}
    return render(request,'enquete.html',context)