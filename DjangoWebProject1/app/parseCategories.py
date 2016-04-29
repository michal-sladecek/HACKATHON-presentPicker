import re
keywords = {}
pattern= re.compile("^[0-9_]+$")
with open('parametre.txt','r') as file:
        for line in file:
            arr = re.findall(r"[\w+]+", line)
            for x in arr:
                if not pattern.match(x):
                    keywords[x] = 1
import pickle
with open('parametre.pickle','wb+') as p:
    pickle.dump(keywords,p)
            
