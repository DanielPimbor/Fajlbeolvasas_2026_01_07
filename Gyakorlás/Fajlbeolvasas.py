autok = []
with open('adatok/autok_listaja.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        auto = {'rendszam': adatok[0], 'tipus': adatok[1], 'kor': int(adatok[2])}
        autok.append(auto)

print(f'{autok=}')

for auto in autok:
    print(f'{auto['rendszam']} - {auto['tipus']} - {auto['kor']}')

#////////////////////////////////////////
#ÉN MEGOLDÁSOM
# autok_kora=[]

# for auto in autok:
#     autok_kora.append(auto['kor'])

# print(max(autok_kora))

#////////////////////////////////////////

#TANÁR ÚR MEGOLDÁSA
legidosebb_auto_kora = autok[0]["kor"]
legidosebb_auto = autok[0]
print(legidosebb_auto_kora)

#Legidősebb
for auto in autok:
    if auto['kor'] > legidosebb_auto_kora:
        legidosebb_auto_kora = auto['kor']
        legidosebb_auto = auto

print(legidosebb_auto_kora)
print(legidosebb_auto)
print(f'{legidosebb_auto['rendszam']} - {legidosebb_auto['tipus']} - {legidosebb_auto['kor']}')

#Legfiatalabb

legfiatalabb_auto = autok[0]
legfiatalabb_auto_kora = autok[0]['kor']

for auto in autok:
    if auto['kor'] < legfiatalabb_auto_kora:
        legfiatalabb_auto_kora = auto['kor']
        legfiatalabb_auto = auto

print(legfiatalabb_auto_kora)
print(f'{legfiatalabb_auto['rendszam']} - {legfiatalabb_auto['tipus']} - {legfiatalabb_auto['kor']}')