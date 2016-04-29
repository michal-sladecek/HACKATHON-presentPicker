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
    if request.method == 'POST':
        print(request.POST)
        parametre = []
        parametre.append(request.POST['fromGender'])
        parametre.append(request.POST['toGender'])
        parametre.append(request.POST['ageCategory'])
        parametre.append(request.POST['relation'])
        print('Parametre'+str(parametre))
        
        items = ShopItem.objects.order_by('?')[:300]
        itemsWithVal = []
        for x in items:
            itemsWithVal.append((getValue(x.pk,parametre),x))
        itemsWithVal.sort(key=lambda tup: tup[0],reverse=True)
        darceky=[]
        for x in range(10):
            darceky.append(itemsWithVal[x][1])
        return render(
            request,
            'app/darceky.html',
            {
                'title':'Appka na darčeky',
                'year':datetime.now().year,
                'darceky':darceky ,
            }
        )  
    return render(request,'app/index.html', {
                'title':'Appka na darčeky',
                'year':datetime.now().year,
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

