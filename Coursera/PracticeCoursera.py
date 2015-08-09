__author__ = 'Pri'
a = ["apple", "banana", "pear"]
print(a)

h = [1, 2, 3]
# print(h)
print type(h)

c = [1, a, 2, 3]
# print(c[0:])

# print(c[:])

things = ['apples', 'orange', 'pear', 'grape', 'kiwi']
# print(things[1:3])

if 'pear' in things:
    print("There is")

if not 'mango' in things:
    print("No")

a = {'name': 'Priyansh', 'Fruits': things}

# del a['name']
print(a['Fruits'][0:2])
