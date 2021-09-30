import sys
# from pkg.pkg import module
from john.math import geo, geo as g

print(g.square_area(55))


print(geo.circle_area(25))
print(geo.square_area(10))
print(geo.rectangle_area(5, 10))

geo._spam()

geo_attrs = [
    attr for attr in dir(geo) if not attr.startswith('_')
]
print(geo_attrs)
print('-' * 60)
# module search
# 1. current folder
# 2. folders in PYTHONPATH if exists
# 3. predefined folders

for path in sys.path:
    print(path)
