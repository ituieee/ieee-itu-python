# Kullanıcıdan istenilen sayıda öğrenci isimleri ve sınav notları alan, ortalamasını hesaplayan, ve harf notu veren bir program yazalım
# sınavlar sırasıyla %10, 20, 30 ve 40 ağırlıklı olsun

students = {} # Verileri tutacağımız boş dictionary 
num = int(input("Öğrenci Sayısı Girin: "))
print("\n")
i = 0
while i < num: # Öğrenci notlarını alacak döngü
    notes = [] # Öğrenci notlarını tutacağımız boş listeyi oluşturuyoruz (döngü 2. kez döndüğü sefer için de listeyi boşaltmış oluyoruz.)
    print("\n")
    name = input("Öğrenci Adı Girin: ")
    j = 0
    while j < 4:
        note = int(input(f"{j + 1}. Sınav Notu: "))
        notes.append(note)
        j += 1
    students[name] = notes # Dictionary içine o öğrenci ve sahip olduğu notlar girildi
    i += 1

avg_notes = {} # Not ortalamalarını tutacağımız değişken

for name, notes in students.items(): # Ortalamaları hesaplayacak döngü
    total = 0 # not toplamını tutacak deiğişken
    for note in notes:
        total += note
    avg = total / len(notes) # Not ortalaması hesabı
    avg_notes[name] = avg # Dictionary içine o öğrenci ve nor ortalaması girildi

grades = {} # Harf notlarını tutacağımız değişken

for name, note in avg_notes.items(): # Harf notlarının atanması
    if note > 90 :
        grade = "A"
    elif note > 70:
        grade = "B"
    elif note > 50:
        grade = "C"
    elif note > 40:
        grade = "D"
    else:
        grade = "F"
    grades[name] = grade

print(grades)



