from django.template import loader
from django.http import HttpResponse
# Create your views here.

def welcome(request):
    template = loader.get_template('welcome.html')
    return HttpResponse(template.render({}, request))

