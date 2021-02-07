# l. List:
#
# Create a simple list

from win32com.client import Dispatch

speak = Dispatch("Sapi.SpVoice")
speak.Speak("Hello guys Welcome to Rupesh Motorworks")

list_SUV = ['Creta', 'Lamborghini Urus', 'Seltos' , 'Range Rover']

print(list_SUV)

#Manipulate the list
list_SUV.append('M.G Hector')

list_SUV.remove('Range Rover')

#Formatted output as string

print('List'+ ', '.join(list_SUV))

# Iterate the list
for SUV in list_SUV:
    print('SUV: '+ SUV)