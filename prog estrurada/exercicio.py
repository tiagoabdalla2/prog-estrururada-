# #03
# def maior(n1,n2):
#     if n1>n2 :
#         return n1
#     return n2 

# def maior2(n1,n2):
#     return n1 if n1> n2 else n2 
# #04
# def vogal(letra): 
#     if letra == "a" or letra == "e" or letra == "i" or letra == "o " or letra == "u":
#         return "é vogal "
#     return "é consoante"

# print(vogal("j"))
# print(vogal("a"))

# def vogal2(letra):
#     match letra :
#         case letra == "a" / "e"/ "i" /"o"/ "u":
#             return "é vogal"
#     return "é consualte"

#05

def calcular_media(n1,n2,n3):
    media=(n1+n2+n3) /3
    if media >= 7:
        sent = "Aprovado! Sua nota foi " + str(media)
    else:
        sent = "Reprovado! Sua nota foi " + str(media)
    return sent 


print(calcular_media(int(input("Digite a primeira nota: ")),int(input("Digite a segunda nota: ")),int(input("Digite a terceira nota: "))))

