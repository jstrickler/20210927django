
i = 0
while i < 3:
    print(i)
    i += 1
print()

while True:
    name = input("Enter name or q to quit: ")
    if name == 'q':
        break
    if name == '':
        print("Please enter a name:")
        continue
    print("Hello,", name)


