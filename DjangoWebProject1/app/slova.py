from .models import ShopItem
import pickle
import os
def idToSlova(id):
    item = ShopItem.objects.get(pk=id)
    file = item.item_file
    present_id = item.item_id
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'idsNaSlova.pickle'),'rb') as f:
        dict = pickle.load(f)
    s = file+present_id
    return dict[s]
    