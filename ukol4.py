#def delka (pocet_cislic):
def pocet_cislic(cislo):
    if len(cislo)==9:
        return True
    if len(cislo)==13 and cislo [:4] == "+420":
        return True
    else:
        return False

#def cena (cena):
def cena_zpravy(text):
    delka_textu=len(text)
    jednotkova_cena=(1+delka_textu//180)*3
    return jednotkova_cena

cislo=input("Vložte telefonní číslo, na které chcete zaslat zprávu: ")
if pocet_cislic(cislo):
    text=input("Zde napište text své zprávy: ")
    cena_textu=cena_zpravy(text)
    print(f"Cena Vaší zprávy je: {cena_textu} Kč.")
else:
    print("Zadané telefonní číslo není uvedeno v platném formátu.")

