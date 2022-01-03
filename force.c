#include <stdio.h>

int main()
{
    int mass, acceleration;

    printf("\nIn this program, we will find force applied on an object using c.\n");
    printf("Formula for force: F = ma (where F is force, m is mass and a is acceleration)\n");
    printf("Enter the mass of the object:\n");
    scanf("%d", &mass);
    printf("Enter the acceleration of the object:\n");
    scanf("%d", &acceleration);

    printf("The force applied on the object is %d Newton\n", mass*acceleration);
    return 0;
}
