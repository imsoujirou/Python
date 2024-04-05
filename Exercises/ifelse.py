# # Problem: Write a program that takes an input temperature in Celsius and checks if it's above or below freezing (0 degrees Celsius).
# If the temperature is above freezing, the program should print "It's above freezing."
# If the temperature is below freezing, it should print "It's below freezing."

# # This problem requires you to use an if-else statement to make a decision based on the input temperature.
# You'll need to compare the input temperature to the freezing point (0 degrees Celsius) and print the appropriate message accordingly.

print("What's the temperature?", end=" ")
temperature = int(input())

if temperature > 0:
    print("It's above freezing")
else:
    print("It's below freezing")