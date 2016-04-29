import re
from collections import defaultdict
keywords={}
import pickle

pattern= re.compile("^[0-9_]+$")
with open('parametre.pickle','rb') as f1:
    dic = pickle.load(f1)
    with open('skupiny.txt','r') as file:
        for line in file:
            keywords[line] = dic
with open('skupinySlova.pickle','wb+') as p:
    pickle.dump(keywords,p)
