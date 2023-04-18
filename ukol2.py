sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
kod=input("Zadej kód součástky: ")
mnozstvi=int(input("Zadej množství součástek: "))

# je/není skladem
if kod in sklad:
    print(f'Součástka {kod} je skladem.')
else:
    print((f'Součástka {kod} není skladem.'))
    exit()

# je skladem, ale je 1. méně / 2. více
if mnozstvi>sklad[kod]:
    print(f'Počet {mnozstvi} kusů požadované součástky {kod} není skladem Lze prodat pouze {sklad[kod]} kusů.')
    del sklad[kod]
else:
    print(f'Poptávku lze uspokojit. Počet {mnozstvi} kusů požadované součástky {kod} je skladem.')
    sklad[kod] -= mnozstvi
    print(f'Zbývá {sklad[kod]} kusů součástky {kod}')
