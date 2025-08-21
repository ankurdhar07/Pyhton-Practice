a = [2, 4, 6]
print(type(a))
print(a[:])
print(a[-3])
print(a[0])

colours = ["Yellow", "Blue", "Red", "Green", "Purple", "Orange", 2, 4, 11, 5, 56, 3 ,3 ,2, 45]
print(colours[2])
print(colours[-3])
print(colours[:])
print(colours[2:4])
print(colours[-2:4])
print(colours[2:-0])
print(colours[2:-1 : 2]) #ans = 'Red', 'Purple'
print(colours[12])

if 11 in colours:
    print("True")
else:
    print("No")

string = "Cow", "Goat", "Dog", "Rabbit", "Bird" # Same thing also applies for string...
if "Rabbit" in string:
    print("True")
else:
    print("No")

Animal = ["Dog", "Bat", "Mouse", "Cow", "Bird", "Tiger", "Lion"]
print(Animal[3:]) #Using positive indexes #ans = Cow -- Lion
print(Animal[:-5]) #Using nagative indexes #ans = Dog -- Bird

Animal = ["Dog", "Bat", "Mouse", "Cow", "Bird", "Tiger", "Lion"]
print(Animal[-3:]) #Using positive indexes #ans = Bird -- Lion
print(Animal[:-2]) #Using nagative indexes #ans = Dog -- Bird

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[4:6]) #Using postive indexes #ans = Pig -- Horse
print(animals[-3:-1]) #Using nagative indexes #ans = Pig -- Goat

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2]) #Using positive indexes #ans = Cat, Bat, Pig, Donkey, Cow
print(animals[-7:-2:2]) #Using nagative indexes #ans = Bat -- Donkey

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[4:6])
# ans = Pig -- Horse

lst = [i for i in range(8)]
print(lst)

lst = [i+1 for i in range (10)]
print(lst)

lst = [i*2 for i in range(10)]
print(lst)

lst = [i+1*2 for i in range(22) if i%2 == 0]
print(lst)

names = ["Suman", "Aryan", "Sonu", "Riya", "Sneha", "Sanu"]
namesWITH_0 = [item for item in names if "S" in item]
print(namesWITH_0)

names = ["Suman", "Aryan", "Sonu", "Riya", "Sneha", "Sanu"]
namesWITH_0 = [item for item in names if len(item) > 4]
print(namesWITH_0)