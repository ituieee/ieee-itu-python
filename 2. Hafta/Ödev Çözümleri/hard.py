alfabe = ["A", "B", "C", "Ç", "D", "E", "F", "G", "Ğ", "H", "I", "İ", "J", "K", "L", "M", "O", "Ö", "P", "R", "S", "Ş", "T", "U", "Ü", "V", "Y", "Z"] # Alfabe tanımlanması
while True:
    new_text = "" # Yeni kelime tutulacak
    islem = input("\n\n---------\n1-Şifreleme\n2-Şifre Çözme\nİşlem Seçiniz: ")
    if islem == "1":
        text = input("Metin Girin: ").upper() #alfabemizdeki harfler büyük oldugu icinupper() ile harfleri büyüttük
        for harf in text:
            index = alfabe.index(harf)
            if (index == len(alfabe) - 1): # Eğer son harfse 
                index = 0 # İlk harfe atanır
            else: # Değilse
                index += 1 # bir sonraki harfe atanır
            new_text += alfabe[index].lower()
        print(f"Şifrelenmiş metin: {new_text}")
    elif islem == "2":
        text = input("Metin Girin: ").upper()
        for harf in text:
            index = alfabe.index(harf)
            if (index == 0): # Eğer ilk harf ise
                index = len(alfabe) - 1 # Son harfe atanır
            else: # Değilse
                index -= 1 # Bir önceki harfe atanır
            new_text += alfabe[index].lower()
        print(f"Şifresi Çözülmüş metin: {new_text}")
    else:
        print("Hatalı işlem!")


    