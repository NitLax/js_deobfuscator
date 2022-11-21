import sys

nomfic = sys.argv[1]
if (nomfic[0:2]==".\\" or nomfic[0:2]=="./"):
    nomfic=nomfic[2:]

f =open(nomfic,"r")
content = f.read()
f.close()
content=content+" "
content2 = ""
indent=0
instring=False
indoublestring=False
intab =False
for i in range(len(content)):
    character = content[i]
    match character:
        case ";":
            if content[i+1]=="}":
                content2 = content2+";"
            else:
                content2=content2+ ";\n"+indent*"\t"
        case "{":
            indent=indent+1
            content2=content2+"{\n"+indent*"\t"
        case "}":
            indent=indent-1
            if content[i+1]==";":
                content2 = content2+"}"
            else:
                content2=content2+"\n"+indent*"\t"+"}\n"+indent*"\t"
        case "'":
            instring = not instring
            content2 = content2 + "'"
        case '"':
            indoublestring=not indoublestring
            content2=content2+'"'
        case "[":
            intab = True
            content2=content2+"["
        case "]":
            intab = False
            content2=content2+"]"
        # case ',':
        #     if (not instring and not indoublestring and not intab):
        #         content2 = content2+',\n'+indent*'\t'
        #     else:
        #         content2 = content2+','
        case _:
            content2=content2+character

f = open(nomfic.split('.')[0]+"_deobf"+'.'+nomfic.split('.')[1],"w+")
f.write(content2)


