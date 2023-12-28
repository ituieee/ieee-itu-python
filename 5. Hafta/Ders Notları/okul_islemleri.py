class Ogrenci:
    def __init__(self, name, clas):
        self.name = name
        self.clas = clas
    
    def info(self):
        print(f"{self.name} öğrencisi {self.clas}. sınıfta okumaktadır.")

siniflar = [1, 2, 3, 4]

def okul_yazdir(name):
    print(f"Okul adı: {name}")

