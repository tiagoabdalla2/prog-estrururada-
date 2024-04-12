"""
uso quando n souber qual exceçao pode subi 
ou qaundo sei qual exeçao pode subir, mas n sei como o codigo chega lá 
"""
def divso(a,b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("erro! calculo n funcionou")
    except TypeError:
        print("erro ambos os parametros precisam ser numereicos. ")

def terceira_letra():
    try:
        nome= input("informe seu nome ")
        print(f"a terceira letra do seu nome é {nome}[2]")
    except Exception as err:
        print("erro desconhecido.")
        ret = "erro!"
    else:
        print("leitura dos dados bem sucedida.")
    finally:
        print("fim da funçao")
        return ret 



# divisao(10, 2 )
# print(terceira_letra()) 
    

  class TamanhoExcedidoError  