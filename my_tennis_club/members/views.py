# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    #template = loader.get_template('myfirst.html')
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse("Hello world from Member View!")