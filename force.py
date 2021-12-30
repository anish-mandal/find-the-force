# Program starts

print("\nIn this program, we will find force applied on an object using python.")
# formula for Force
print("Formula for force: F = ma (where F is force, m is mass and a is acceleration)\n")

# While loop to keep checking for the value if entered an invalid value
while(True):
    try:
        mass = int(input("Enter the mass of the object: "))
        break
    except:
        print("You can only use mass as number.")

# Again while loop to keep checking for the value if entered an invalid value
while(True):
    try:
        acceleration = int(input("Enter the acceleration of the object: "))
        break
    except:
        print("You can only use acceleration as number.")

# Answer 
print(f"The force applied on the object is {mass*acceleration} Newton")

# Program ends
