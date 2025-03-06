# Zoe Jimenez, FizzBuzz PYTHON
x = 1

while x <= 50:
    if x % 3 and x % 5:
        print("FizzBuzz")
    elif x % 5:
        print("Buzz")
    elif x % 3:
        print("Fizz")
    else:
        print(x)
    x+= 1