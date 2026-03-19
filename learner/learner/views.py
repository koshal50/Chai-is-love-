from django.http import HttpResponse
from django.shortcuts import render

from performer.models import chaiVariety
from performer.models import about_description

# def home(request): #created a request to later on call the home function 
#     return HttpResponse("hello world, you are at home page")

#imported render from django shortcuts and then created a index.html file in templates folder then chaanged setting templates.dirs to os.path.join(BASE_DIR, 'templates')
def home(request): 
     chais = chaiVariety.objects.all()[:8]
     chai_dict = {chai.id: chai for chai in chais}

     return render(request, "home.html", {"chai_dict": chai_dict})

def about(request): #created a request to later on call the about  function 
    abouts = about_description.objects.all()
    return render(request, "about.html", {"abouts": abouts})

def contact(request): #created a request to later on call the contact  function 
    return render(request, "contact.html")

