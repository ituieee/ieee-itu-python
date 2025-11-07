'''
Bu örneğimizde, tüm öğrendiklerimizi kullanarak bir öğrencinin verilerini alan ve yazdıran bir program hazırlayacağız.

Alışmak için değişken tanımlamaları ingilizce yapılmıştır, bildiğimiz üzere değişken isimlerini keyfi yapabiliriz, ancak ingilizce yapmaya alışmanız daha sağlklı olur.

'''
# Öğrenci bilgilerini almak için kullanıcıdan input alıyoruz
ad = input("Ad: ")
soyad = input("Soyad: ")
faculty = input("Fakülte: ")
department = input("Bölüm: ")
gpa = input("Ortalama: ")

# Alınan bilgileri düzenli bir şekilde ekrana yazdırıyoruz
print("\n") # Bir satır boşluk bırakmak için \n özel karakteri kullanılır
print("="*24) 
print("---Öğrenci Bilgileri---")
print("="*24) 
print("\n") 
print(f"Okulumuz öğrencilerinden {ad} {soyad}, {faculty} Fakültesi {department} Bölümünde okumaktadır ve {gpa} ortalamaya sahiptir.")