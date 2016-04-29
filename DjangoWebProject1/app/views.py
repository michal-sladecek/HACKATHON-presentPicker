"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest,HttpResponseRedirect
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
        if 'isGood' in request.POST:
            feedback(request.POST['primaryKey'],parametre,request.POST['isGood'])
            HttpResponseRedirect(ShopItem.objects.get(pk==request.POST['primaryKey']).url)
        items = ShopItem.objects.order_by('?')[:100]
        itemsWithVal = []
        for x in items:
            itemsWithVal.append((getValue(x.pk,parametre),x))
        itemsWithVal.sort(key=lambda tup: tup[0],reverse=True)
        darceky=[]
        for x in range(12):
            darceky.append(itemsWithVal[x][1])
        return render(
            request,
            'app/darceky.html',
            {
                'title':'Appka na darčeky',
                'year':datetime.now().year,
                'darceky':darceky ,
                'fromGender': parametre[0],
                'toGender': parametre[1],
                'ageCategory': parametre[2],
                'relation': parametre[3],
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

