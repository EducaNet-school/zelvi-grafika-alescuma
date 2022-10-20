seznamos = [1,2,3,4,5,6,7,8,9,10]

mista = int(input("O kolik míst?"))
seznamos = seznamos[mista:] + seznamos[:mista]

def řada(rada):
    for i in range(0, len(rada)):
        print(řada[i], end=' ')
    
    # print("Na jakou stranu?")
#řada
#Dodělat možnost na jakou stranu chceme.
print(seznamos)
