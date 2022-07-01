# Random module
# Mersenne Twister es el algoritmo para generar valores aleatorios en python
import random

random_integer = random.randint(1,10)
print(random_integer)

# Valores entre 0.0 y 1.0
random_float = random.random()
# Valores entre 0.0 y 5.0
random_float * 5



random_site = random.randint(0,1)
if random_site == 1:
    print("Heads")
else:
    print("Tails")



# Lists
# Estructura para alamecenar datos en Python
states_of_Mexico = ["Mexico City","Sinaloa","Yucatan"]
print(states_of_Mexico[1])
print(states_of_Mexico[-1])

states_of_Mexico[2] = "Campeche"
states_of_Mexico.append("Morelos")
states_of_Mexico.extend(["Yucatan","Sonora","Nuevo Leon"])



# Random bill
names = input("Names of friends: ")
names = names.split(", ")
random_int = random.randint(0,len(names)-1)
print(f"{names[random_int]} will pay the bill today!")
# Or
print(f"{random.choice(names)} will pay the bill tomorrow!")


# Nested lists
row1 = ["1","2","3"]
row2 = ["4","5","6"]
row3 = ["7","8","9"]
nested_list = [row1,row2,row3]
print(nested_list[1][2])

row1 = ["O","O","O"]
row2 = ["O","O","O"]
row3 = ["O","O","O"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
coordinates = input("Insert the coordinates: ")
horizontal = int(coordinates[0]) - 1
vertical = int(coordinates[1]) - 1
map[vertical][horizontal] = "X"
print(f"{row1}\n{row2}\n{row3}")









