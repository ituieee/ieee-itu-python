class Sekil:
    def __init__(self, kenar_sayisi):
        self.kenar_sayisi = kenar_sayisi
    
    def ic_acilar_toplamı(self):
        return (self.kenar_sayisi - 2) * 180
    
    def bir_ic_aci(self):
        d = self.ic_acilar_toplamı()
        return d / self.kenar_sayisi
    
besgen = Sekil(5)
print(besgen.ic_acilar_toplamı())
print(besgen.bir_ic_aci())