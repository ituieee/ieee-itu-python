"""
Bu örnekte basit bir hesap makinesi yapacağız.
Kullanıcıdan iki sayı ve bir işlem alıp, sonucu göstereceğiz.
"""

print("=" * 30)
print("  Basit Hesap Makinesi")
print("=" * 30)

# İlk sayıyı alalım
sayi1 = float(input("\nBirinci sayıyı girin: "))

# İkinci sayıyı alalım
sayi2 = float(input("İkinci sayıyı girin: "))

# İşlem türünü alalım
print("\nİşlem seçin:")
print("1. Toplama (+)")
print("2. Çıkarma (-)")
print("3. Çarpma (*)")
print("4. Bölme (/)")

islem = input("\nİşlem numarasını girin (1-4): ")

# İşlemi gerçekleştirelim
if islem == "1":
    sonuc = sayi1 + sayi2
    islem_simge = "+"
elif islem == "2":
    sonuc = sayi1 - sayi2
    islem_simge = "-"
elif islem == "3":
    sonuc = sayi1 * sayi2
    islem_simge = "*"
elif islem == "4":
    if sayi2 != 0:
        sonuc = sayi1 / sayi2
        islem_simge = "/"
    else:
        print("Hata: Sıfıra bölme yapılamaz!")
        exit()
else:
    print("Geçersiz işlem!")
    exit()

# Sonucu yazdıralım
print(f"\nSonuç: {sayi1} {islem_simge} {sayi2} = {sonuc}")
