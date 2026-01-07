"""1. Feladat
A mellékelt fájl néhány ismert programozási nyelv adatát tartalmazza. Olvasd be a fájl tartalmát és tárold el
a, egy listában, melynek elemei szótárak,
b, egy kétdimenziós listában!
mind a két esetben az évszám int típusként kerüljön rögzítésre! """

list_of_programming_languages= []
with open('1 Feladat/Timeline_of_ programming_languages.csv', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        programming_language = {'year': int(adatok[0]), 'programming language': adatok[1], 'first name': adatok[2], 'last name of chief developer': adatok[3]}
        list_of_programming_languages.append(programming_language)

print(f'{list_of_programming_languages=}')

for programming_language in list_of_programming_languages:
    print(f'{programming_language['year']} - {programming_language['programming language']} - {programming_language['first name']} - {programming_language['last name of chief developer']}')

#/////////////////////////////////////////

#Legfiatalabb

youngest_language = list_of_programming_languages[0]
youngest_language_year = list_of_programming_languages[0]['year']

for programming_language in list_of_programming_languages:
    if programming_language['year'] > youngest_language_year:
        youngest_language_year = programming_language['year']
        youngest_language = programming_language

print('\n')
print('This is the year when youngest language in the list was invented.')
print(youngest_language_year)
print('This is the data of the youngest language in the list.')
print(f'{youngest_language['year']} - {youngest_language['programming language']} - {youngest_language['first name']} - {youngest_language['last name of chief developer']}')

#/////////////////////////////////////////

#Legidősebb

oldest_language = list_of_programming_languages[0]
oldest_language_year =list_of_programming_languages[0]['year']

for programming_language in list_of_programming_languages:
    if programming_language['year'] < oldest_language_year:
        oldest_language_year = programming_language['year']
        oldest_language = programming_language


print('\n')
print('This is the year when oldest language in the list was invented.')
print(oldest_language_year)
print('This is the data of the oldest language in the list.')
print(f'{oldest_language['year']} - {oldest_language['programming language']} - {oldest_language['first name']} - {oldest_language['last name of chief developer']}')


