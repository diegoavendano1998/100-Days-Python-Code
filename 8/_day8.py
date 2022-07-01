def greeting(name):
    print(f"Hello {name}")
greeting("Diego")
greeting(name="Diego")
# name    -> param
# Diego   -> Argument




def prime_checker(number):
    for divisor in range(2,number):
        if number%divisor == 0:
            return False
    return True

n=8
print(prime_checker(number=n))









