dol = int(input("dol hranice "))
hor = int(input("hor hranice: "))
1
for num in range(dol,hor+1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)

#pekne zjisteni prvocisel, jen chybi ulozeni do seznsmu 