import xml.etree.ElementTree
e = xml.etree.ElementTree.parse('stylezuzana.xml').getroot()
with open("parametre.txt","a+") as file:
    for atype in e.findall('SHOPITEM'):
        try:
            file.write("stylezuzana "+atype.find('ITEM_ID').text+" "+str(atype.find('CATEGORYTEXT').text.split("| "))+"\n")
        except:
            continue
