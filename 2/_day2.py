# Enteros
number = 123456
# Se pueden separar los numero con _ para mejor comprension, pero no afecta en nada al numero
comma_separated_number = 123_123_234

# Flotantes 
number = 213.45

# Booleanos
bool = True
bool = False

print(type(123))
print(type("123"))
print(type(str(123)))

number = 23
first_digit = number[0]
second_digit = number[1]
total = int(first_digit)+int(second_digit)

3+5
7-4
3*2
6/3
2**8 # Exponente
# Respeta la jerarquia de operaciones aritmeticas y ()

# Redondear un numero
print(int(8/3))
print(round(8/3))
print(round(8/3, 2))
# Truncar un numero (similar a int())
print(8 // 3)
# Residuo de una division
print (8%3)
# Operaciones sobre una variable directamente
res = 4 / 2
res /= 2
res += 1
res -= 1
print("Result is "+str(res))
# fstrings lo castea a str en automatico
print(f"Result is {res}")



# Exercise
age_as_int = 22
years_remaining = 90 -age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message = f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months"
print (message)













