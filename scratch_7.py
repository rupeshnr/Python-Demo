# Python 3.4.3. Using MacOS (Version 10.12.5)
# Username and Password...
# The programs purpose: A user must enter the correct username and password for a site called FaceSnap...
# The correct username is elmo and the correct password is blue.


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

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

speak("We have en number of Supercars as well as  SUV cars we have limited edition of Limousines")
speak("and it's our pleasure to show our cars \n  " )

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




