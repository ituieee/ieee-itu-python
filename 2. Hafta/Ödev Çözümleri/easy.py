baskentler = {"Türkiye" : "Ankara", "Rusya" : "Moskova", "Azerbaycan" : "Bakü"}
liste = []
for x, y in baskentler.items(): # Key ve value lara erişmek için
    liste.append(x)
    liste.append(y)
i = 1
while i < (len(liste) + 1): # -1 den -6. elemana kadar erişiyoruz
    print(liste[-i])
    i += 1