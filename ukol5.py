from statistics import mean
teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
prumer=[mean(den) for den in teploty]
print(prumer)

# pokud bych chtěla použít průměr bez importu modulu statistics
# prumer2=[(sum(den)/len(den)) for den in teploty]
# print (prumer2)

rano=[den[0] for den in teploty]
print(rano)

noc=[den[-1] for den in teploty]
print(noc)

# už nevím, proč jsi v tom kódu použil [-1], nicméně s [3] to funguje taky :)
# noc2=[den[3] for den in teploty]
# print(noc2)

poledne_noc=[[den[1], den [3]] for den in teploty]
print(poledne_noc)
