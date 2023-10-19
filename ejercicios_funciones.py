### EJERCICIOS FUNCIONES 1 ###
#DEFINICION DE FUNCIONES

def most(a,b):
    if(x>y):
        return a
    else:
        return b

def least(a,b):
    if(x<y):
        return x
    else:
        return y

#PROGRAMA PRINCIPAL

x = int(input('Un numero: '))
y = int(input('Otro Numero: '))

print(most(x-3, least(x+2,y-5)))