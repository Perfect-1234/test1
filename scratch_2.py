print("Welcome To Our Collation Center")
atiku = str(input("Enter the result for Atiku: "))
buhari = str(input("Enter the result for Buhari: "))
print("****************************************")
if atiku > buhari:
    print("Atiku has won the election with the total of "+atiku +" Votes")
    print("****************************************")
elif atiku < buhari:
    print("Buhari has won the election with the total of "+buhari + " Votes")
    print("****************************************")
elif atiku == buhari:
    print("There is a Tie")
    statewinner = str(input("Enter the winner of more states: "))
    inconclusive = int(input("Enter the number of inconclusive states: "))
    if inconclusive >= 5:
        print("The Election has been cancelled due to high number of inconclusive states")
    elif inconclusive <= 4:
        print("The winner of the Election is "+statewinner)
    else: print("You have entered an invalid number")
else: print("You have entered an invalid number")