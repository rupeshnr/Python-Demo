# inline input

print("Hi guys welcome to Rupesh's Code")
print("Before going to fun , visit our showroom.")
# Python 3.4.3. Using MacOS (Version 10.12.5)
# Username and Password...
# The programs purpose: A user must enter the correct username and password for a site called FaceSnap...
# The correct username is elmo and the correct password blue


print("Please enter your username and password to verify it is you")

userName = input("Hello! Welcome to Rupesh MotorWorks! \n\nUsername: ") #Ask's the User for Username input
password = input("Password: ") # Ask's the user for their password


count = 0 # Create a variable, to ensure the user has limited attempts at entering their correct username and password
count += 1 # The user has already had one attempt above, therefore count has been incremented by 1 already.


while userName == userName and password == password: # The Input will always lead to this while loop, so we can see if their username and password is wrong or correct.


    if count == 3: # Counter, to make sure the user only gets a limited number (3)of attempts
        print("\nThree Username and Password Attempts used. Goodbye") # Lets the user know they have reached their limit
        break # Leave the Loop and the whole program


    elif userName == 'Rupesh' and password == 'Honey': # The userName and password is equal to 'elmo' and 'blue', which is correct, they can enter FaceSnap!
        print("Welcome! ") # Welcomes the User, the username and password is correct
        break # Leave the loop and the whole program as the username and passowrd is correct


    elif userName != 'Rupesh' and password != 'Honey': # The userName and password is NOT equal to 'elmo' and 'blue', the user cannot enter FaceSnap
        print("Your Username and Password is wrong!") # Lets the user know that the Username and password entered is wrong.
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password
        count += 1 # Increments the count by 1
        continue # Continue, as the user hasn't managed to get their username and password correct yet


    elif userName == 'Rupesh' and password != 'Honey': # The userName is equal to 'elmo', but password is NOT equal to 'blue', the user cannot enter FaceSnap
        print("Your Password is wrong!") # Lets the user know that their password is wrong
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password
        count += 1 # increments the count by 1
        continue # Continue, as the user hasn't managed to get their username and password correct yet

print("We have en number of Supercars , SUV cars , and we have a limited edition of Limousines")
print("and it's our pleasure to show our cars \n  " )
# l. List:
#
# Create a simple list
list_SUV = ['Lamborghini Urus', 'Hyundai Creta', 'Kia Seltos' , 'Range Rover']

print(list_SUV)

#Manipulate the list
list_SUV.append('M.G Hector Gloster')

list_SUV.remove('Range Rover')

#Formatted output as string

print('List'+ ', '.join(list_SUV))

# Iterate the list
for SUV in list_SUV:
    print('SUV: '+ SUV)

# l. List:
#
# Create a simple list
list_SuperCars = ['Bugatti Divo', 'Lamborghini Sian', 'Ferrari 812', 'Bugatti Chiron', 'Lamborghini Terzo']

print(list_SuperCars)

# Manipulate the list
# list_SuperCars.append('Bugatti Veyron')

list_SuperCars.remove('Bugatti Chiron')

# Formatted output as string

print('List' + ', '.join(list_SuperCars))

# Iterate the list
for SuperCar in list_SuperCars:
    print('SuperCar: ' + SuperCar)

# l. List:
#
# Create a simple list
list_Limousine = ['Cadillac Limousine', 'The American Dream', 'Mercedes-Maybach S600 Pullman Guard', 'Rolls Royce Phantom Limousine', 'Mercedes G63 Armored Limousine']

print(list_Limousine)

# Manipulate the list
list_Limousine.append('Sultan Of Brunei’s Rolls Royce')

list_Limousine.remove('The American Dream')

# Formatted output as string

print('List' + ', '.join(list_Limousine))

# Iterate the list
for Limousine in list_Limousine:
    print('Limousine: ' + Limousine)



class Car:
    print("And let us show you car Colour and it's Price with it's Speed")
    def __init__(self,name):
        self.name=name
class SuperCar (Car): # inheritance
    def getSpeed(self):
        print("Maximum Speed 350")
    def price(self):
        print(" and price 25million US $")
    def colour(self):
        print("with extraordinary colour Blue Dragon ")


class SuperCar2(Car):  # inheritance
    def getSpeed(self):
        print("Maximum Speed 370")
    def price(self):
        print(" and price 30million US $")
    def colour(self):
        print("with extraordinary colour NightFury a black colour ")


class Limousine(Car):  # inheritance
    def getSpeed(self):
         print("Maximum Speed 250")
    def price(self):
        print(" and price 35million US $")
    def colour(self):
        print("with extraordinary colour using pure Gold ")


class SUV (Car): # inheritance
    def getSpeed(self):
        print("Maximum Speed 300")
    def price(self):
        print(" and price 22million US $")
    def colour(self):
        print("with extraordinary colour Red Phoenix ")

class SUV2 (Car):  # inheritance
    def getSpeed(self):
        print("Maximum Speed 250")
    def price(self):
        print(" and price 1million US $")
    def colour(self):
        print("with extraordinary colour Red Phoenix ")

carLst = [SuperCar("SuperCar: Lamborghini Sian"), SuperCar2("SuperCar: Bugatti Divo") , SUV("SUV: Lamborghini Urus"), SUV2 ("SUV: Kia Seltos") ,  Limousine("Limousine: Mercedes G63 Armored Limousine")]
for car in carLst:
    print(car.name+":",end="")
    car.getSpeed()
    car.price()
    car.colour()


print("If you want anything more call us on : + 9 1 3 4 3 2 5 7 0 3 1 6 and our website w w w.Rupesh MotorWorks.com")


name =input("Type get your name \n")
print("Hello \n")
print("Hi", name)
age = int(input("Enter your age "))
if age >= 18:
    print("You are eligible for artificial Intelligence")
else:
    if age >= 10:
        print(" You are eligible for Beginners Python Tutorial")
    else:
        print("You are not eligible for Python coding or artificial Intelligence ")

print("The below is given an mathematical coding")

favourite = int(input("Enter your favourite number "))

print(name, 'and')
place = input("Type your place \n")

print("I'am an assistance robot to help you to sort a greater and smallest number as well as odd or a even number .")
print("and it's my pleasure to help you ")
print(" I'am an guide to sort the greater number and smallest number  ")
print("I'am a friendly robot that you could also create mathematical tech like me")
print("Now enter down some numbers so we could find greater numbers")
a = int(input("Enter a  number:"))
b = int(input("Enter a  number:"))
c = int(input("Enter a  number:"))
if a > b and a > c:
        print(a, 'is the greatest number')
elif b > a and b > c:
        print(b, 'is the greatest number')
else:
        print(c, 'is the greatest number')

print("Now enter down some numbers so we could find smallest numbers")
a = int(input("Enter a  number"))
b = int(input("Enter a  number"))
c = int(input("Enter a  number"))
if a < b and a < c:
    print(a, 'is the smallest number')
elif b < a and b < c:
    print(b, 'is the smallest number')
else:
    print(c, 'is the smallest number')



print("Now let's check whether the number is odd or even / 3 chance to type a number and check whether it is odd/even.")
num = int(input("Enter any number: "))
flag = num % 2
if flag == 0:
    print(num, "is an even number")

elif flag == 1:
    print(num, "is an odd number")
else:
    print("Error, Invalid input")
num = int(input("Enter any number: "))
flag = num % 2
if flag == 0:
    print(num, "is an even number")
elif flag == 1:
    print(num, "is an odd number")
else:
    print("Error, Invalid input")

num = int(input("Enter any number: "))
flag = num % 2
if flag == 0:
    print(num, "is an even number")
elif flag == 1:
    print(num, "is an odd number")
else:
    print("Error, Invalid input")

    print("Now it’s an while loop statement , to end click 0")
lst = []
c = input("Enter 1 to add elements to list  and 0 to exit program \n ")
while c != "0":
    lst.append(c)
    c = input("Enter an element to add elements to list and 0 to exit loop ")
print(lst)

print("Vowels counting machine ")

word = input("Enter word")
count = 0
for i in word:
    if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        count += 1
print("number of vowels in %s is %d " % (word, count))

print("This is another way to find vowels but with consonants")


# Python Program to Count Vowels and Consonants in a String

str1 = input("Please Enter Your Own String : ")
vowels = 0
consonants = 0

for i in str1:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
            or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print("Total Number of Vowels in this String = ", vowels)
print("Total Number of Consonants in this String = ", consonants)


print("Now let's calculate numbers using +addition , -subtraction , *  multiplication , / division")

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ch, num2, ":", result)

print("The another way arithmetic operation is given below.")
print("The below statement show of + add , - sub , x mul , / div , // floor_div , ** power , % modulus . ")
print("Now let's see how this operation works .")


num1 = int(input('Enter First number: '))
num2 = int(input('Enter Second number '))
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
floor_div = num1 // num2
power = num1 ** num2
modulus = num1 % num2
print('Sum of ',num1 ,'and' ,num2 ,'is :',add)
print('Difference of ',num1 ,'and' ,num2 ,'is :',sub)
print('Product of' ,num1 ,'and' ,num2 ,'is :',mul)
print('Division of ',num1 ,'and' ,num2 ,'is :',div)
print('Floor Division of ',num1 ,'and' ,num2 ,'is :',floor_div)
print('Exponent of ',num1 ,'and' ,num2 ,'is :',power)
print('Modulus of ',num1 ,'and' ,num2 ,'is :',modulus)



print("Now let's see how the positive and negative numbers sorter / Only 5 chance.")






num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

import time  # Imports a module to add a pause

# Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

# Grabbing objects
sword = 0
flower = 0

required = ("\nUse only A, B, or C\n")  # Cutting down on duplication

print("Here are some fun questions for you")

# The story is broken into sections, starting with "intro"
def intro():
    print("After a drunken night out with friends, you awaken the "
          "next morning in a thick, dank forest. Head spinning and "
          "fighting the urge to vomit, you stand and marvel at your new, "
          "unfamiliar setting. The peace quickly fades when you hear a "
          "grotesque sound emitting behind you. A slobbering orc is "
          "running towards you. You will:")
    time.sleep(1)
    print("""  A. Grab a nearby rock and throw it at the orc
  B. Lie down and wait to be mauled
  C. Run""")
    choice = input(">>> ")  # Here is your first choice.
    if choice in answer_A:
        option_rock()
    elif choice in answer_B:
        print("\nWelp, that was quick. "
              "\n\nYou died!")
    elif choice in answer_C:
        option_run()
    else:
        print(required)
        intro()


def option_rock():
    print("\nThe orc is stunned, but regains control. He begins "
          "running towards you again. Will you:")
    time.sleep(1)
    print("""  A. Run
  B. Throw another rock
  C. Run towards a nearby cave""")
    choice = input(">>> ")
    if choice in answer_A:
        option_run()
    elif choice in answer_B:
        print("\nYou decided to throw another rock, as if the first "
              "rock thrown did much damage. The rock flew well over the "
              "orcs head. You missed. \n\nYou died!")
    elif choice in answer_C:
        option_cave()
    else:
        print(required)
        option_rock()


def option_cave():
    print("\nYou were hesitant, since the cave was dark and "
          "ominous. Before you fully enter, you notice a shiny sword on "
          "the ground. Do you pick up a sword. Y/N?")
    choice = input(">>> ")
    if choice in yes:
        sword = 1  # adds a sword
    else:
        sword = 0
    print("\nWhat do you do next?")
    time.sleep(1)
    print("""  A. Hide in silence
  B. Fight
  C. Run""")
    choice = input(">>> ")
    if choice in answer_A:
        print("\nReally? You're going to hide in the dark? I think "
              "orcs can see very well in the dark, right? Not sure, but "
              "I'm going with YES, so...\n\nYou died!")
    elif choice in answer_B:
        if sword > 0:
            print("\nYou laid in wait. The shimmering sword attracted "
                  "the orc, which thought you were no match. As he walked "
                  "closer and closer, your heart beat rapidly. As the orc "
                  "reached out to grab the sword, you pierced the blade into "
                  "its chest. \n\nYou survived!")
        else:  # If the user didn't grab the sword
            print("\nYou should have picked up that sword. You're "
                  "defenseless. \n\nYou died!")
    elif choice in answer_C:
        print("As the orc enters the dark cave, you sliently "
              "sneak out. You're several feet away, but the orc turns "
              "around and sees you running.")
        option_run()
    else:
        print(required)
        option_cave()


def option_run():
    print("\nYou run as quickly as possible, but the orc's "
          "speed is too great. You will:")
    time.sleep(1)
    print("""  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned town""")
    choice = input(">>> ")
    if choice in answer_A:
        print("You're easily spotted. "
              "\n\nYou died!")
    elif choice in answer_B:
        print("\nYou're no match for an orc. "
              "\n\nYou died!")
    elif choice in answer_C:
        option_town()
    else:
        print(required)
        option_run()


def option_town():
    print("\nWhile frantically running, you notice a rusted "
          "sword lying in the mud. You quickly reach down and grab it, "
          "but miss. You try to calm your heavy breathing as you hide "
          "behind a delapitated building, waiting for the orc to come "
          "charging around the corner. You notice a purple flower "
          "near your foot. Do you pick it up? Y/N")
    choice = input(">>> ")
    if choice in yes:
        flower = 1  # adds a flower
    else:
        flower = 0
    print("You hear its heavy footsteps and ready yourself for "
          "the impending orc.")
    time.sleep(1)
    if flower > 0:
        print("\nYou quickly hold out the purple flower, somehow "
              "hoping it will stop the orc. It does! The orc was looking "
              "for love. "
              "\n\nThis got weird, but you survived!")
    else:  # If the user didn't grab the sword
        print("\nMaybe you should have picked up the flower. "
              "\n\nYou died!")


intro()

print("This is 33 question quiz and get full mark in quiz. ")

import time

true = ["T", "t", "True"]
false = ["F", "f", "False"]
correct = 0  # Storing the correct answers

name = input("What's your name?")  # Storing the user's name

print("\nOK, " + name + ", let's get started. Remember, the following answers are only True or False.")
time.sleep(2)

print("\n1. Cyclones spin in a clockwise direction in the southern hemisphere.")
choice = input(">")
if choice in true:
    correct += 1  # If correct, the user gets one point
else:
    correct += 0

print("\n2. Goldfish only have a memory of three seconds.")
choice = input(">")
if choice in false:
    correct += 1
else:
    correct += 0

print("\n3. The capital of Libya is Benghazi.")
choice = input(">")
if choice in false:
    correct += 1
else:
    correct += 0

print("\n4. Dolly Parton is the godmother of Miley Cyrus.")
choice = input(">")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n5. Roger Federer has won the most Wimbledon titles of any player.")
choice = input(">")
if choice in false:
    correct += 1
else:
    correct += 0

print("\n6. An octopus has five hearts.")
choice = input(">")
if choice in false:
    correct += 1
else:
    correct += 0

print("\n7. Brazil is the only country in the Americas to have the official language of Portuguese.")
choice = input(">")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n8. The Channel Tunnel is the longest rail tunnel in the world.")
choice = input(">")
if choice in false:
    correct += 1
else:
    correct += 0

print("\n9. Darth Vader famously says the line “Luke, I am your father” in The Empire Strikes Back.")
choice = input(">")
if choice in false:
    correct += 1
else:
    correct += 0

print("\n10. Olivia Newton-John represented the UK in the Eurovision Song Contest in 1974, the year ABBA won with “Waterloo”.")
choice = input(">")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n11. Stephen Hawking declined a knighthood from the Queen.")
choice = input(">")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n12. The highest mountain in England is Ben Nevis.")
choice = input(">")
if choice in false:
    correct += 1
else:
    correct += 0

print("\n13. Nicolas Cage and Michael Jackson both married the same woman.")
choice = input(">")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n14. Japan and Russia did not sign a peace treaty after World War Two so are technically still at war.")
choice = input(">")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n15. The mathematical name for the shape of a Pringle is hyperbolic paraboloid.")
choice = input(">")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n16. Charlie Chaplin came first in a Charlie Chaplin look-alike contest.")
choice = input(">")
if choice in false:
    correct += 1
else:
    correct += 0

print("\n17. Michael Keaton’s real name is Michael Douglas.")
choice = input(">")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n18. Napoleon was of below-average height.")
choice = input(">")
if choice in false:
    correct += 1
else:
    correct += 0

print("\n19. Donald Duck’s middle name is Fauntelroy.")
choice = input(">")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n20. The Statue of Liberty was a gift from France.")
choice = input(">")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n21. According to Scottish law, it is illegal to be drunk in charge of a cow.")
choice = input(">")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n22. The Great Wall of China is visible from space.")
choice = input(">")
if choice in false:
    correct += 1
else:
    correct += 0

print("\n23. The first tea bags were made of silk.")
choice = input(">")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n24. Meghan Markle’s first name is Rachel.")
choice = input(">")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n25. Warsaw is the capital of Bulgaria.")
choice = input(">")
if choice in false:
    correct += 1
else:
    correct += 0

print("\n26. A metre is further than a yard.")
choice = input(">")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n27. A woman has walked on the moon.")
choice = input(">")
if choice in false:
    correct += 1
else:
    correct += 0

print("\n28. Flying in an aeroplane is statistically safer than driving in a car.")
choice = input(">")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n29. John Challis plays Boycie in Only Fools and Horses.")
choice = input(">")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n30. Valletta is the capital of Cyprus.")
choice = input(">")
if choice in false:
    correct += 1
else:
    correct += 0

print("\n31. The currency of France is the Franc.")
choice = input(">")
if choice in false:
    correct += 1
else:
    correct += 0

print("\n32. Ben Nevis is the tallest mountain in the UK.")
choice = input(">")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n33. Radio head wrote the song Love is All Around.")
choice = input(">")
if choice in false:
    correct += 1
else:
    correct += 0

print ("\nYou're finished, " + name + ". You got", correct , "out of 33 correct.")

print("Thank you make a tech like me , I was created by your son and have a nice day", name)

print("Thank you")

