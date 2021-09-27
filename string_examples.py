
s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''

print("It's a bad thing")
print('It is a "bad" thing')
print("It is a \"bad\" thing")
print("""It's a "bad" thing""")

query = """
select *
from customers
where state = 'NC'
"""


s5 = r"spam\n"  # raw string
print(s5)


print(len(s1), len(s2), len(s5))

print(s1)
print("wombat")
print(repr(s1))

x = "platypus         "
print(x)
print(repr(x))

m = 'abc'






