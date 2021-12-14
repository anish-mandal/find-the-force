# Program starts

print("\nIn this program, we will find force applied on an object using python.")
# formula for Force
print("Formula for force: F = ma (where F is force, m is mass and a is acceleration)\n")

# True variable to stop the while loop
true = True
# While loop to keep checking for the value if entered an invalid value
while(true is True):
    try:
        mass = int(input("Enter the mass of the object: "))
        true = False
    except:
        print("You can only use mass as number.")

# True variable to stop the while loop
true_again = True
# Again while loop to keep checking for the value if entered an invalid value
while(true_again is True):
    try:
        acceleration = int(input("Enter the acceleration of the object: "))
        true_again = False
    except:
        print("You can only use acceleration as number.")

# Answer 
print(f"The force applied on the object is {mass*acceleration} Newton")

# Program ends