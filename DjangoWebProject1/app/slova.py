from .models import ShopItem
import pickle
def idToSlova(id):
    item = ShopItem.objects.get(pk=id)
    file = item.item_file
    present_id = item.item_id
    with open('idsNaSlova.pickle') as f:
        dict = pickle.load(f)
    s = file+present_id
    return dict[s]
    