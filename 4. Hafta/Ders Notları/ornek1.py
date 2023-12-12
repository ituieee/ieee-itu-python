# Araçların bilgileriin tutan bir sınıf oluşturalım.

class Vehicle: # Parent Class oluşturulması
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def display_info(self):
        print(f"Araç: {self.brand} {self.model}")
    

class Car(Vehicle): # Arabalar için child class oluşturulması
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model) # Önce parent class'ın fonksiyonu çağrılır
        self.num_doors = num_doors

    def display_info(self):
        super().display_info() # Önce parent class'ın fonksiyonu çağrılır
        print(f"Tür: Araba, Kapı Sayısı: {self.num_doors}")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, num_wheels):
        super().__init__(brand, model) # Önce parent class'ın fonksiyonu çağrılır
        self.num_wheels = num_wheels

    def display_info(self):
        super().display_info() # Önce parent class'ın fonksiyonu çağrılır
        print(f"Tür: Motosiklet, Tekerlek Sayısı: {self.num_wheels}")

# Sınıflardan objelerin oluşturulması
vehicle1 = Vehicle("Generic", "Vehicle")
car1 = Car("Toyota", "Corolla", 4)
motorcycle1 = Motorcycle("Harley-Davidson", "Sportster", 2)

# Bilgilerin gösterilmesi
vehicle1.display_info()
print("\n")
car1.display_info()
print("\n")
motorcycle1.display_info()