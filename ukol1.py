# úkol:
jmeno="Barbora"
email = jmeno + "@czechitas.cz"
print(email)

# nepovinný bonus:
jmeno_a_prijmeni=input("Zadejte své jméno a příjmení:")
jmeno, prijmeni = jmeno_a_prijmeni.split()
print(jmeno_a_prijmeni.upper())
print(jmeno_a_prijmeni.lower())
print(jmeno.capitalize(), prijmeni.capitalize())
print(jmeno[0].upper() + ".", prijmeni[0].upper() + ".")
if len(jmeno) > 5:
    print(jmeno[0].upper() + ".", prijmeni.capitalize())
else:
    print(jmeno.capitalize(), prijmeni.capitalize())