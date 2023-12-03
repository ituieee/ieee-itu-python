ilanlar = {}
while True: # Sürekli olarak çalışması için
    print("\n\n---------")
    secim = input("- İlan Eklemek: 1\n- İlan Çıkartmak:2\n- Çıkış: 3\nYapmak istediğiniz işlemi seçin: ")
    if (secim == "1"):
        ad = input("İlan Adı Girin: ")
        if(ad in ilanlar.keys()): # Eğer böyle bir ilan adı zaten varsa, hata döner.
            print("Bu adlı bir ilan zaten var.")
            continue
        marka = input("Araba Markası Girin: ")
        model = input("Araba Modeli Girin: ")
        yıl = input("Araba yılını girin: ")
        fiyat = input("Araba fiyatını girin: ")
        ozellikler = { # Bu özelliklerin bir dict içerisinde birleştirilmesi
            "marka" : marka,
            "model" : model,
            "yıl" : yıl,
            "fiyat" :  fiyat
        }
        ilanlar[ad] = ozellikler # ilanlara yeni girdi eklenmesi
    
    elif (secim == "2"):
        ad = input("Çıkaracağınız ilan adı seçin: ") 
        if(not ad in ilanlar.keys()): # Eğer böyle bir ilan yoksa hata döner
            print("Böyle bir ilan yok!")
            continue
        del ilanlar[ad]
    
    elif (secim == "3"):
        print("Çıkılıyor...")
        break
    
    else:
        print("Hatalı işlem numarası!")

    