#!/bin/bash

echo "In this program, we will find force applied on an object using bash script."
echo "Formula for force: F = ma (where F is force, m is mass and a is acceleration)"


echo "Enter the mass of the object: " 
read MASS
echo "Enter the acceleration of the object: " 
read ACCELERATION

RESULT=$(($MASS*$ACCELERATION))

echo "The force applied on the object is $RESULT Newton"