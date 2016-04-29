"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import ShopItem
from .slova import *
def home(request):
    """Renders the home page."""    
    assert isinstance(request, HttpRequest)
    darceky_na_zobrazenie = ShopItem.objects.all().order_by('?')[:12]
    for x in darceky_na_zobrazenie:
        print(x.product+" "+str(idToSlova(x.pk)))
    return render(
        request,
        'app/darceky.html',
        {
            'title':'Appka na darčeky',
            'year':datetime.now().year,
            'darceky': darceky_na_zobrazenie,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def darceky(request):
    assert isinstance(request,HttpRequest)

