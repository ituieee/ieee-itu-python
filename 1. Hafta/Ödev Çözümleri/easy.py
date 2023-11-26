ad = input("Ad: ").capitalize()
soyad = input("Soyad: ").capitalize()
crn = input("CRN: ")
ders = input("Ders Adı:").upper()
vize1 = float(input("Birinci Vize Notunuz: "))
vize2 = float(input("İkinci Vize Notunuz: "))
final = float(input("Final Notunuz: "))

ortalama = round(((vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4)), 1)

print(f"Okulumuz öğrencilerinden {ad} {soyad}, {crn}-{ders} dersinden {ortalama} ortalamaya sahiptir.")