print("Součet lichého čísla ")

start = int(input("dolni hranice (Jen liche) : "))
end   = int(input("horni hranice (Jen liche) : "))

vysledek=0

for x in range(start,end):
    if(x % 2 == 1):
        vysledek=vysledek+x
        
print("Součet lichých čísel je ",vysledek)
