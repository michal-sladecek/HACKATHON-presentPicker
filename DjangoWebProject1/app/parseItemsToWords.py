import re
from collections import defaultdict
keywords = defaultdict(list)

pattern= re.compile("^[0-9_]+$")
with open('parametre.txt','r') as file:
        for line in file:
            arr = re.findall(r"[\w+]+", line)
            keywords[arr[0]+arr[1]].append(arr[0])
            for x in arr[2:]:
                if not pattern.match(x):
                    keywords[arr[0]+arr[1]].append(x)
import pickle
with open('idsNaSlova.pickle','wb+') as p:
    pickle.dump(keywords,p)
