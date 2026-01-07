nyelvek=[]
with open('1 Feladat/Timeline_of_ programming_languages.csv', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        year = int(adatok[0])
        language = adatok[1]
        first_name = adatok[2]
        last_name = adatok[3]
        nyelvek.append([year, language, first_name, last_name])

print(nyelvek)

legidosebb_nyelv = nyelvek[0]
legidosebb_nyelv_evszam = nyelvek[0][0]

for nyelv in nyelvek:
    if nyelv[0] < legidosebb_nyelv_evszam:
        legidosebb_nyelv_evszam = nyelv[0]
        legidosebb_nyelv = nyelv

print(legidosebb_nyelv)
print(legidosebb_nyelv_evszam)


legfiatalabb_nyelv = nyelvek[0]
legfiatalabb_nyelv_evszam = nyelvek[0][0]

for nyelv in nyelvek:
    if nyelv[0] > legfiatalabb_nyelv_evszam:
        legfiatalabb_nyelv_evszam = nyelv[0]
        legfiatalabb_nyelv = nyelv

print(legfiatalabb_nyelv)
print(legfiatalabb_nyelv_evszam)