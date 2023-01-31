import sys
import re
import jsbeautifier

docnom = sys.argv[1]
newnom = docnom.split(".js")[0] + "_deobfuscated.js"

doc = open(docnom,"r")
obfuscated_code = doc.read()
doc.close()


def desobfuscate_js(obfuscated_code):
    
    #finding all var and function
    x = re.findall("_0x([0-9|a-f]+)",obfuscated_code)
    x = list(set(x))
    x = sorted(x, key=lambda el:len(el))
    x.reverse()
    #print(obfuscated_code)

    #renaming var and function
    noVar = 1
    noFct = 1
    for var in x:
        if re.search("function _*0x"+var,obfuscated_code):
            obfuscated_code=re.sub("_*0x"+var,"fct"+str(noFct),obfuscated_code)
            noFct +=1
        else:
            obfuscated_code=re.sub("_*0x"+var,"var"+str(noVar),obfuscated_code)
            noVar +=1
    
    #calculating remaining hexa values
    #re.findall("\( *0x[0-9|a-f]+ *[\+|\-|]\)")
    #oui=re.findall("\( ?[+-]? ?0x[0-9|a-f]+ ?[?[\+\-\/\*] ?[+-]? ?0x[0-9|a-f]+ ?]* ?\)",obfuscated_code)
    oui=re.findall("\( ?[+-]? ?0x[0-9|a-f]+ ?[[+-/\*]? ?[+-]? ?0x[0-9|a-f]+ ?]{0,5}",obfuscated_code)
    print(oui)

    ## attention certaine var usee une seule fois -> calucl aussi?



    #x = re.sub("function _*0x([0-9|a-f]+)","function fct_\g<1>",obfuscated_code)
    #x = re.sub("_*0x([0-9|a-f]+)( *= *function\(\))","fct_\g<1>\g<2>",obfuscated_code)
    #a = "35e8c8"
    #print(bytes.fromhex(a).decode('utf-8'))
    return obfuscated_code 


beautified_code = jsbeautifier.beautify(obfuscated_code)

beautified_code = desobfuscate_js(beautified_code)

newdoc = open(newnom,"w")
newdoc.write(beautified_code)
newdoc.close()
