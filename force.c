// C libraries
#include <stdio.h>

// Program starts
int main()
{
    /*
    This program does not contain exception handling cause C does not have exception handling..
    */

    printf("\nIn this program, we will find force applied on an object using python.\n");
    printf("Formula for force: F = ma (where F is force, m is mass and a is acceleration)\n");

    int mass;
    printf("Enter the mass of the object:\n");
    scanf("%d", &mass);

    int acceleration;
    printf("Enter the acceleration of the object:\n");
    scanf("%d", &acceleration);

    printf("The force applied on the object is %d Newton\n", mass*acceleration);
    return 0;
    // Program ends
}