num = int(input("Zadejte číslo, které chcete pro násobilku použít:"))

print("Malá nasobilka čísla:", num)
for i in range(1, 11):
   print(num,"X",i,"=",num * i)

# moc pekne formatovani print, neukladas do seznamu