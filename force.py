print("\nIn this program, we will find force applied on an object using python.")
print("Formula for force: F = ma (where F is force, m is mass and a is acceleration)\n")

while(True):
    try:
        mass = int(input("Enter the mass of the object: "))
        break
    except:
        print("You can only use mass as number.")

        
while(True):
    try:
        acceleration = int(input("Enter the acceleration of the object: "))
        break
    except:
        print("You can only use acceleration as number.")
 
print(f"The force applied on the object is {mass*acceleration} Newton")
