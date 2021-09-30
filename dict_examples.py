d1 = dict()  # empty dict
d2 = {'a': 5, 'm': 16, 'e': 12, 'r': 99}
d3 = {}
d4 = dict(a=5, m=16, e=12, r=99)
data = [('a', 5), ('m', 16), ('e', 12), ('r', 99)]
d5 = dict(data)
print(d2)
print(d4)
print(d5)

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}
print(airports['EWR'], airports['RDU'], airports['YOW'])
print(airports.get('LAX'))
print(airports.get('LAX', 'Not found'))
airports['LAX'] = "Los Angeles"
airports['IAH'] = "Houston"
airports['MCO'] = "Disney World"
print(airports, '\n')

more_airports = {'JAX': 'Jacksonville', 'MIA': 'Miami'}
airports.update(more_airports)
print(airports, '\n')

del airports['IAH']

print(airports, '\n')

for code in 'JAX', 'ABC', 'YOW', 'DEF', 'RDU':
    print(code, code in airports)
print()

for code, airport_name in sorted(airports.items()):
    print(code, airport_name)
print()
print(airports.items(), '\n')

print(len(airports))











