from django.shortcuts import render
import xml.etree.ElementTree
from app.models import ShopItem
from django.http import HttpResponse

import os
# Create your views here.
files = ['detskahracka','kupma','stylezuzana','gastroset']
def populateView(request):
    i = 0
    for file in files:
        print(os.path.join(os.path.dirname(os.path.realpath(__file__)),'xmls',file+'.xml'))
        e = xml.etree.ElementTree.parse(os.path.join(os.path.dirname(os.path.realpath(__file__)),'xmls',file+'.xml')).getroot()
        for atype in e.findall('SHOPITEM'):
            try:
                item = ShopItem()
                item.item_file = file
                item.item_id = atype.find('ITEM_ID').text
                item.product = atype.find('PRODUCT').text
                item.description = atype.find('DESCRIPTION').text
                item.url = atype.find('URL').text
                item.imgurl = atype.find('IMGURL').text
                item.price_vat = atype.find('PRICE_VAT').text
                item.save()
                i+=1
                if i%100==0:
                    print("Milestone..."+str(i))
            except:
                continue
    return HttpResponse("Databaza by mala byt plna sraciek")

                        
        