def test():
    n = 15

    # for i in range(1,n+1):
    #     if not i%3==0 and not i%5==0:
    #         print(i)
    #     elif i%3==0 and i%5==0:
    #         print("FizzBuzz")
    #     elif i%3==0:
    #         print("Fizz")
    #     else:
    #         print("Buzz")
    10 - 3
    11 - 1
    12 - 3
    13 - 1
    14 - 1
    15 - 3
    16 - 3

    15

    for i in range(1,n+1):
        if not i%3==0 and not i%5==0:
            print(i)
        elif i%5==0:
            if i%3!=0:
                print("Buzz")
            else:
                print("FizzBuzz")
        else:
            print("Fizz")

    10 - 3
    11 - 1
    12 - 2
    13 - 1
    14 - 1
    15 - 3
    16 - 2

    14 


    for i in range(1,n+1):
        if i%3>0:
            if i%5==0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif i%3==0:
            if i%5==0:
                print("FizzBuzz")
            else:
                print("Buzz")
        else: 
            print(i)

    10 - 2
    11 - 1
    12 - 3
    13 - 1
    14 - 1
    15 - 3


"""
1     
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
"""







def costo(n=1000):
    result = 0
    for i in range(1,n):
        if i%5 == 0:
            result += 3
        elif i%3 == 0:
            result += 2
        else:
            result += 1
    print(f"result: {result}")





def matriz_3_5(n=15):
    m_5 = []
    m_3 = []
    count = 0
    for i in range(1,n,5):
        print(i)
        m_5.append([i for i in range(i,i+5)])
    print(m_5)

matriz_3_5()


