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
    listCalculHex=re.findall("([+-]?0x[0-9|a-f]+( ?[+-/\*] ?[+-]?0x[0-9|a-f]+)*)",obfuscated_code)
    for calcul in listCalculHex:
        print(calcul[0]," = ",eval(calcul[0]))
        obfuscated_code = obfuscated_code.replace(calcul[0],str(eval(calcul[0])))

    ## attention certaine var usee une seule fois -> calucl aussi? pas tout de suite au moins

    #obfuscated_code = re.sub("\((\d+)\)[^;]","\g<1>",obfuscated_code)
    return obfuscated_code 


beautified_code = jsbeautifier.beautify(obfuscated_code)

beautified_code = desobfuscate_js(beautified_code)

newdoc = open(newnom,"w")
newdoc.write(beautified_code)
newdoc.close()
