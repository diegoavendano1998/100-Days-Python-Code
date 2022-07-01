from art import logo


def add(first_num,second_num):
    return first_num+second_num
def substract(first_num,second_num):
    return first_num-second_num
def multiply(first_num,second_num):
    return first_num*second_num
def divide(first_num,second_num):
    return round(first_num/second_num,2)

print(logo)
operators = {
            "+":add,
            "-":substract,
            "*":multiply,
            "/":divide
            }
finish = False



first_number = input("First number: ")
while not finish:
    print("Operators: ",*operators)
    operator = input("Pick un operator: ")
    second_number = input("Second number: ")
    if operators.get(operator,False):
        method = operators[operator]
        try:
            first_number = method(float(first_number),float(second_number))
            cont = "no"
            if first_number:
                cont = input(f"\nThe result is {first_number}\nDo you want to do another operation with that number? [yes/no] ")
            if cont == "no":
                finish = True
        except:
            print("\nInvalid number")
    else:
        print("\nInvald operator")
print("Bye ;)")









