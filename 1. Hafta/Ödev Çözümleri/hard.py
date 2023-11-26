#Faiz hesabı

anaPara = input("Ana para: ")
vade = input("Vade: ")
yillikFaizOrani = input("Yıllık faiz oranı: ")
sonuc = round((float(anaPara)/100)*(float(yillikFaizOrani)/12)*(float(vade)))
print(f"{vade} ay sonunda, yıllık %{yillikFaizOrani} faiz oranı ile {anaPara}TL ana paradan {sonuc}TL faiz geliri elde edilecektir.")



