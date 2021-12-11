# program_starts

print("\nIn this program, we will find force applied on an object using python.")
# formula_for_Force
print("Formula for force: F = ma (where F is force, m is mass and a is acceleration)\n")

# true_variable_to_stop_the_while_loop
true = True
# while_loop_to_keep_checking_for_the_value_if_entered_an_invalid_value
while(true is True):
    try:
        mass = int(input("Enter the mass of the object: "))
        true = False
    except:
        print("You can only use mass as number.")

# true_variable_to_stop_the_while_loop
true_again = True
# again_while_loop_to_keep_checking_for_the_value_if_entered_an_invalid_value
while(true_again is True):
    try:
        acceleration = int(input("Enter the acceleration of the object: "))
        true_again = False
    except:
        print("You can only use acceleration as number.")

# answer_
print(f"The force applied on the object is {mass*acceleration} Newton")

# program_ends