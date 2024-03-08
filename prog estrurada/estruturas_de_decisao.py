# def saudaçao(turno):
#     if turno == "M" :
#         print ("Bom Dia !")
#     elif turno == "T":
#         print ("boa tarde !")
#     elif turno == "N":
#         print ("boa noite ")
#     else: 
#         print ("dados invalidos ")
# def saudaçao2(turno):
#     if turno == "M"
#         return "bom dia "
#     if turno == "T"
#         return "boa tarde"
#     if turno == "N"
#         return "boa noite "
    
    

# saudaçao("N")
# saudaçao("M")
# saudaçao("T")
# saudaçao("A")

# print ("-" * 30)
# saudaçao2 ("M")
# saudaçao2 ("T")
# saudaçao2 ("N")

# def le_nome():
#     nome = input ("informe o seu nome ")
#     #if nome == "":
#     if not nome : 
#         print ("erro ! entrada invalida")
#     return nome

#terminario

def e_par(num):
    if num % 2 :
        return "é impar"    
    return "é par "

def e_par(num):
    return" È impar " if num % 2 else "é par "


def saudaçao3(turno):
    match turno:
        case "M":
            print ("bom dia !" )
        case "T":
            print ("boa tarde!")
        case "N":
            print ("boa noite !")
        case _ : #defalte case , opcional 
            print ("dado ivalido")



saudaçao3 ("M")
saudaçao3("N")
saudaçao3("T")
