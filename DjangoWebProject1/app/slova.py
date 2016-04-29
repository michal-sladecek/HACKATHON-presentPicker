from .models import ShopItem
import pickle
import os
from math import log
def idToSlova(id):
    item = ShopItem.objects.get(pk=id)
    file = item.item_file
    present_id = item.item_id
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'idsNaSlova.pickle'),'rb') as f:
        dict = pickle.load(f)
    s = file+present_id
    return dict[s]

def getValue(id, params):
    value = 0
    words = idToSlova(id)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'skupinySlova.pickle'),'rb') as f:
        dict = pickle.load(f)
    for parameter in params:
        for word in words:
            value += dict[parameter][word]
    return value

def feedback(id, params, val):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'skupinySlova.pickle'),'rb') as f:
        dict = pickle.load(f)
    words = idToSlova(id) 
    if val==1:
        for parameter in params:
            for word in words:
                dict[parameter][word]+=1
    if val==0:
        for parameter in params:
            for word in words:
                dict[parameter][word]-=5
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'skupinySlova.pickle'),'wb') as f:
        pickle.dump(dict,f)          
        
    
 
    