import 'dart:core';
import 'dart:io';

main() {
  late num mass; 
  late num acceleration;
  print("\nIn this program, we will find force applied on an object using dart.");
  print("Formula for force: F = ma (where F is force, m is mass and a is acceleration)\n");

  while(true){
    print("Enter value of mass: ");
    try {
      String? massString = stdin.readLineSync();
      if (massString != null) mass = int.parse(massString);
    } catch (e) {
      print("You can only use mass as number");
      continue;
    }
    break;
  }

  while(true){
    print("Enter value of acceleration: ");
    try {
      String? accelerationString = stdin.readLineSync();
      if (accelerationString != null) acceleration = int.parse(accelerationString);
    } catch (e) {
      print("You can only use acceleration as number");
      continue;
    }
    break;
  }

  print("The force applied on the object is ${mass*acceleration} Newton");
}