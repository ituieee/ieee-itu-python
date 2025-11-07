# Küsüratlı sayılara yuvarlama işlemi yapan bir fonksiyon tanımlayacağız. Bu fonksiyona değer olarak yuvarlanamayacak bir girdi(sayı olmayan) verilirse, bu hatayı yakalamaya çalışacağız.

def yuvarla(sayi, basamak):
    basamak = int(basamak)
    try:
        float(sayi) 
    except ValueError:
        print("Lütfen Doğru formatta bir sayı giriniz.")
        return
    try:
        int(basamak)
    except:
        print("Lütfen geçerli bir basamak sayısı girin.")
        return
    try:
        tam_kisim = sayi.split(".")[0]
        küsürat = sayi.split(".")[1]
    except:
        print("Yuvarlama işlemi için ondalık bir sayı girmelisiniz.")
        return
    if(basamak == 0):
        return int(tam_kisim)
    else:
        if(int(küsürat[basamak - 1]) < 5):
            yuvarlak_küsürat = küsürat[:basamak]
        else:
            x = str(int(küsürat[basamak - 1]) + 1)
            yuvarlak_küsürat = küsürat[:basamak - 1] + x
        sonuc = float(tam_kisim + "." + yuvarlak_küsürat)
        return sonuc

sayi = input("Yuvarlanacak sayıyı girin: ")
basamak = input("Yuvarlanacak basamak sayısı girin: ")

sonuc = yuvarla(sayi, basamak)
print(sonuc)

    
