#NUMBER 1:
print("NUMBER 1")
for x in range(101):
    print(f'{x} -- My name is Udoh Daniel Perfect')

print("-------------------------------------------------------------------------------------------------------------")
#NUMBER 2:
print("NUMBER 2")
for num in range(21):
    num_sqr = num*num
    print(f'{num} -- {num_sqr}')

print("-------------------------------------------------------------------------------------------------------------")
#NUMBER 3:
print("NUMBER 3")
#3a:
print("3a")
number = [20, 2, 2, 20]
for count in number:
    if count == 20:
        print(f'*' * count)
    else:
        print(f'*' + f'                  ' + f'*')

#3b:
print("3b")
triangle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for count in triangle:
    print(f'*'  * count)

#3c:
print("3c")
for ro in range(4):
    if ro == 0:
        print(f'    ' + f'*' + f'    ')
    if ro == 1:
        print(f'   ' + f'*' + f' ' + f'*' + f'   ')
    if ro == 2:
        print(f'  ' + f'*' + f' ' +f'*' + f' ' + f'*' + f'  ')
    if ro == 3:
        print(f'*' + f'       ' + f'*' + f'   ')

print("-------------------------------------------------------------------------------------------------------------")
#NUMBER 4:
print("NUMBER 4")
n = int(input("Enter a number n: "))
def factorial(n):
    if n== 1:
        return 1
    else:
        s = n * factorial(n-1)
        #print(f'The {n}th factorial is {s}')
        return s
f = pow(3, factorial(n))
print(f'f(n)=(3^n!): f({n})= {f}')

print("-------------------------------------------------------------------------------------------------------------")
#NUMBER 5:
print("NUMBER 5")
def factorial(n):
    if n== 1:
        return 1
    else:
        s = n * factorial(n-1)
        print(f'The {n}th factorial is {s}')
        return s
print(factorial(5))



