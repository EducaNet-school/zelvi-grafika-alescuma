
fcisla = int(input("Kolik chcete?"))

c1, c2 = 0, 1
vypoc = 0


if fcisla <= 0:
   print("POUZE KLADNÉ")

elif fcisla == 1:
   print("Fibonacci řada max",fcisla,":")
   print(c1)

else:
   print("Fibonacci řada:")
   while vypoc < fcisla:
       print(c1)
       nth = c1 + c2

       c1 = c2
       c2 = nth
       vypoc += 1

 #Dodělatz list až dojdu dom
 # tiskne mene, nez pozaduji, 0 nepatri do rady
