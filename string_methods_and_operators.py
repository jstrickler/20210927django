
actor = 'Chris Hemsworth'

print(len(actor))

a1 = actor.upper()
print(a1)
print(actor.upper())
a = 'apple'
b = 'banana'
print(a + b)
print(actor.startswith('Chris'))
print(actor.startswith('Liam'))
print("ort" in actor)
print("bluz" in actor)
print(actor.find('Hem'))
print(actor.index('Hem'))
print(actor.replace('Chris', 'Liam'))

s = "fa   la la    la"
print(s.split())

s = "a::b::c::d"
print(s.split('::'))

s = 'foo,bar,blah\n,baz\nbarf'
print(s.replace('\n', '').split(','))

print(actor)
print(actor.lower().count('h'))

s = "  \t    \t   All my exes live in Texas  \t  "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s = "xyxxxxyyyyxyxyyyyyyyyAll my exes live in Texasyyyyyyyyyx"
print("|" + s.lstrip("xy") + "|")
print("|" + s.rstrip("xy") + "|")
print("|" + s.strip("xy") + "|")
print()




