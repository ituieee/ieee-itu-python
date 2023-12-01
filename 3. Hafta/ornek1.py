#### Aldığı tüm elemanları toplayan bir fonksiyon yazacağız.
def liste_topla(*args):
    toplam = 0
    for sayi in args:
        toplam += sayi
    return toplam

print(liste_topla(99,6,3))
sonuc = liste_topla(1, 2, 3, 4, 5, 6)
print(sonuc)

