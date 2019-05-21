# Strings in Python
# name = "Udoh Daniel"
# print(name[0])
'''
#num1 = "55"
#print(type(num1))
#num2 = int(num1)
#print(type(num2))
'''
'''
x = 'blue'
y = 'green'
z = x
print(x,y,z)
z=y
print(x,y,z)
x=z
print(x,y,z)
'''
'''
Collection data types 
1. List: mutable
'''
'''
days = ['monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
days[0] = days
print(days)

#2. Tuples: unmutable
countries=('Nigeria', 'The UK', 'Togo', 'Australia')
#countries[2]="Lagos"
print(countries)

print(len("Daniel"))
print(len(["momday", "tuesday", False, 501]))'''
 #while loop
'''
lessThan5 = 0
while lessThan5 < 5:
    print("Still < 5")
    lessThan5 += 1
    if lessThan5 == 3:
        break
    print("Thank you")
print("finished")
'''
'''
countries = ["Nigeria", "Ghana", True, 1000, "America"]
i = 0
while i<len(countries):
    print(countries[i])
    i += 1
'''
'''
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
vowels = "AEIOU"
for A in alphabets:
    if A in vowels:
        print(A, "is a vowel")
    else:
        print(A, "is a consonant")
'''

'''x = (input("enter a string"))
result = x+" " + "additional part"
print(result)'''
'''
try:
    x = int(input("enter a number: "))
    answer = x/2
    print(answer)
except ValueError as err:
    print(err)
    '''
'''
list1 = ["mango", "orange", "cashew", "onion"]
list2 = ["tamato", 20]
print(list1 + list2)
list2 += ["cherry", "bannas"]
print(list2)
'''

#returns the sum of all valid inputs
#drops all invalid inputs politely
'''total = 0
count = 0
while True:
    try:
        line = input("enter a number: ")
        if line:
            try:
                number = float(line)
            except ValueError as ve:
                print(ve)
                continue
            total += number
            count += 1
        print(total)
    except EOFError:
        break'''
#Using Functions:
'''def add():
    a=float(input("enter first number: "))
    b=float(input("enter second number: "))
    print(a+b)
add()
'''
'''
def get_int():
        try:
            i = int(input("Enter a number or something convertible: "))
            print("your age is ", i)
        except ValueError as ve:
            print(ve)
get_int()
'''
'''
list1 = ['daniel', 'tony', 'science', True, 123]
print(list1.count("tony"))

for x in list1:
    if(list1.index(x) < 3):
        print(x, end=' and ')
    else:
        print(x)
'''
'''
#index
names = ['bolaji', 'aisha', 'daniel', 'david', 'aisha', 'taofeek']
print('first occurence of Aisha: ', names.index('aisha'))

#POP
subjects = ['Mathematics', 'Science', 'physics', 'english', 'language', 'religion']
print(subjects.pop())
'''
'''
#remove
subjects = ['Mathematics', 'Science', 'physics', 'english', 'language', 'religion']
holder = subjects.pop()
holder = subjects.remove('Science')
print(subjects)
'''

'''
#reverse: reverses the list and returns none
subjects = ['Mathematics', 'Science', 'physics', 'english', 'language', 'religion']
print(subjects.reverse())
print(subjects)
print(subjects.reverse())
print(subjects)

#sort
subjects = ['Mathematics', 'science', '1234', 'physics', 'english', '24', 'Language', 'religion']
subjects.sort()
print(subjects)
'''

#DICTIONARIES
'''
states_pop = {"Lagos": 3567234, "Kano": 4674281, "Abuja":
              233322, "Port-Hacourt": 166627, "Kaduna": 255892}

print(states_pop['Kano'])
'''
'''
word = input("enter a number from 1 to 5 in either English, Yoruba or Igbo: ")
en_yor = {'one':'ookan', 'two':'eeji', 'three':'eeta', 'four':'eerin', 'five':'aarun'}

yor_ibo = {'ookan':'otu', 'eeji':'abuo', 'eeta':'ato', 'eerin':'ano', 'aarun':'ise'}


for k , v in en_yor.items():
    print(k + v)
for k, v in yor_ibo.items():
    print(k + v)

#print(yor_ibo[en_yor['one']])
if word in en_yor or yor_ibo:
    print(yor_ibo[en_yor[word]])
'''

#Rules
#we cant use mutable types as keys



#operations of dictionaries
'''
en_yor = {'one':'ookan', 'two':'eeji', 'three':'eeta', 'four':'eerin', 'five':'aarun'}
yor_ibo = {'ookan':'otu', 'eeji':'abuo', 'eeta':'ato', 'eerin':'ano', 'aarun':'ise'}
#en_yor.__delitem__('one')
del en_yor['two']
print('two' in en_yor)
print('ookan' in yor_ibo)
print(en_yor)
'''
'''
morse = {
    'A': ": qw",
    'B': ": qwer",
    'C': ": qwerty",
    'D': ": qwertyui",
    'E': ": qwertyuiop",
    '1': ": as",
    '2': ": asd",
    '3': ": asdf",
    '4': ": asdfg",
    '5': ": asdfghj"
}

#pop
en_yor = {'one':'ookan', 'two':'eeji', 'three':'eeta', 'four':'eerin', 'five':'aarun'}
yor_ibo = {'ookan':'otu', 'eeji':'abuo', 'eeta':'ato', 'eerin':'ano', 'aarun':'ise'}

word = input("enter an english number from 1 to 5: ")
print("This is your Igbo pronounciatio: ", yor_ibo[en_yor[word]])
'''

#popitem()
'''capitals = {"Nigeria":"Abuja", "Ghana":"Accra", "Togo":"Lome", "South Africa":"Johannesburg", "Mali":"Bamako"}
print(capitals.popitem())
print(capitals.popitem())
print(capitals.popitem())
print(capitals.popitem())
print(capitals.popitem())
for k, v in capitals.items():
    print(k+": "+v)'''

#conversion between lists and dictionaries
'''
capitals = {"Nigeria":"Abuja", "Ghana":"Accra", "Togo":"Lome", "South Africa":"Johannesburg", "Mali":"Bamako"}
list1 = list(capitals)
print(list1)
print(type(capitals))
print(list1[2])'''

#FUNCTIONS
'''
#simply prints the arguments passed to it
def writer(word):
    print(word)
writer("Hello class")

#converts celsius to farenheit:
def faren(T_in_celsius):
    return T_in_celsius *(9/5) + 32
print(faren(20), "farenheit")
(****************************************)
faren_list = []
celsius_list = [20, 15, 17, 30, 40]
for x in celsius_list:
    faren_list.append(faren(x))
print(faren_list)

numlist = [20, 15, 17, 30, 40]
f = []
for x in numlist:
    f.append(faren(x))
print(f)
(****************************************)
'''
'''
#change a list passed to it:
def chnager(listX):
    return(listX.append([10, 30, 40, 50, 60]))
print(chnager([0, 3, 8, 4]))
'''
'''
def average():
    list1 = []
    sum = 0
    x = 0
    while(len(list1) < 5):
        item = float (input("enter a number: "))
        list1.append(item)
        x += 1
    for item in list1:
        sum += item
    avg = float(sum/len(list1))
    print(avg)
average()'''
#SETS
#CREATING SETS
'''
x = set("A python set")
#print(x)
print(type(x))
#passed a list to the inbuilt set() function
y = set(["Python", "C++", "Java", "Javascript", "PHP"])
print(y)
#when a tuple contains repeated items is passed to the set() fxn
states = set(("Lagos", "Benin", "Onitsha", "Kaduna", "Benin", "Bayelsa"))
print(states)
#we cannot include mutable objects during set creation
#classes = set("js1", ['ss1', 'ss2', 'ss3'], "js2", "js3")'''

#SETS OPERATION
#ADD OPERATION
'''colors = {"Red", "Green", "Blue"}
colors.add("Brown")
colors.add("Blue")
print(colors)

print("-----------------------------------------------------------------------")
#CLEAR OPERATION
states = {"Lagos", "Benin", "Onitsha", "Kaduna", "Benin", "Bayelsa"}
states.clear()
print(states)
#remove()
print(states.remove("Onitsha"))
print(states)

print("-----------------------------------------------------------------------")
#copy()
more_states = {"Ogun", "Imo", "Nasarawa", "Kaduna", "Adamawa"}
more_states_backup = more_states.copy()
print(more_states_backup)

print("-----------------------------------------------------------------------")
#difference
A = {"Tomi", "Daniel", "Ejiro", "Salah"}
B = {"Daniel", "Mohammed", "Bolaji", "Kayode"}
#print(A - B)
print(A.difference(B))
#print(B - A)
print(B.difference(A))

print("-----------------------------------------------------------------------")
#difference_update
x = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
y = {'c', 'f', 'b'}
z = {'e', 'd', 't', 'o'}
#print(x.difference_update(y))
print(x)
print(x-y-z)
print("-----------------------------------------------------------------------")

#discard()
x = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
x.discard('b')
print(x)
print("-----------------------------------------------------------------------")

#intersection
x = {'a', 'b', 'c', 'd', 'e'}
y = {'c', 'd', 'e', 'f', 'g'}
print(x.intersection(y))
print(x.union(y))
print("-----------------------------------------------------------------------")

#disjoint()
print(x.isdisjoint(y))
print("-----------------------------------------------------------------------")

#subset()
x = {'a', 'b', 'c', 'd', 'e'}
y = {'c', 'd'}
print(y.issubset(x))
print(x.issubset(y))'''

#KEYWORD PARAMETERS
'''def sum(a, b, c=0, d=0):
    return a-b+c-d
print(sum(12, 4))
print(sum(12,4,5))

#VARIABLE SCOPING: by default, variables defined in a funtion are local to that
def f():
    print(s)
s="pyhton"
f()
def f():
    s= 'clojure'
    print(s)
f()
def f():
    #print(s)
    s='perl'
    print(s)
s="python"
f()
print(s)

def f():
    global s
    print(s)
    s='dog'
    print(s)
s='cat'
f()
print(s)'''

#ARBITRARY number of parameters
'''def arithmetic_mean(first, *values):
    return (first + sum(values)) / (1 + len(values))
print(arithmetic_mean(45, 32, 89, 78))'''

'''def sum_of_gp():
    r = float(input("enter the radius: "))
    a = float(input("enter the first term: "))
    n = float(input("enter the nth term: "))

    if (r < 1):
        print((a * (1 - pow(r,n))) / (r - 1))
    elif (r > 1):
        print((a*(pow(r,n) - 1)) / (r - 1))
    else:
        print("Your Radius is equal to 1")
        exit()
sum_of_gp()
def average(*values):
    print((sum(values)) / (len(values)))
average(3,2,4)'''

'''#Recursive funtions
def factorial(n):
    if n== 1:
        return 1
    else:
        print("the factorial is ", n)
        return n*factorial(n-1)
print(factorial(5))'''
