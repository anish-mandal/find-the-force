#include <iostream>
#include <typeinfo>
using namespace std;

int main() {
    int mass, acceleration;

    cout<<"In this program, we will find force applied on an object using python."<<endl<<"Formula for force: F = ma (where F is force, m is mass and a is acceleration)\n"<<endl;

    cout<<"Enter the mass of the object: ";
    cin>>mass;
    cout<<"Enter the acceleration of the object: ";
    cin>>acceleration;

    cout<<"The force applied on the object is "<<mass*acceleration<<" Newton"<<endl;
    return 0;
}