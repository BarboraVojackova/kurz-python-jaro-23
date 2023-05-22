class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self. registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True

    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return "Potvrzuji zapůjčení vozidla."
        else:
            return "Vozidlo není k dispozici."
        
    """
    # Bonus (vrácení auta):
    def vrat_auto(self, stav_tachometru, pocet_dni):
        self.stav_tachometru = stav_tachometru
        self.pocet_dni = pocet_dni
        self.dostupne = True
        cena = 400 * pocet_dni if pocet_dni < 7 else 300 * pocet_dni
        return f"Cena za půjčení auta je {cena} Kč."
    """

    def info(self):
        return f"Registrační značka: {self.registracni_znacka}, Značka a typ vozidla: {self.typ_vozidla}"

auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534")
auto2 = Auto("1P3 4747", "Škoda Octavia", "41253")

vyber = input("Zadejte značku vozidla (Peugeot/Škoda): ")

if vyber == "Peugeot":
    auto = auto1
elif vyber == "Škoda":
    auto = auto2
else:
    print("Takové auto nemáme.")

print(auto.info())
print(auto.pujc_auto())

# Pokus o druhé půjčení
print(auto.pujc_auto())

"""
# Bonus (vrácení auta):
stav_tachometru = int(input("Zadejte stav tachometru při vrácení auta: "))
pocet_dni = int(input("Zadejte počet dní, po které jste auto používal: "))

print(auto.vrat_auto(stav_tachometru, pocet_dni))
"""