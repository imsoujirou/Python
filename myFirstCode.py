# This program says hello and asks for my name

# Notes
#print is to display 
#input is to input 
#len is string length
#data types string, int, float

print('Hello World!')
print('What is your name?') # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of you name is')
print(len(myName))
print('What is your age?') # ask for age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')