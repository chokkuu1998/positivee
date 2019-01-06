#include<stdio.h>
#include<conio.h>

int main() {
    float fahren, celsius;

    printf("Enter the temperature in celsius\n");
    scanf("%f", &celsius);

    /* convert celsius to fahreneheit 
  * Multiply by 9, then divide by 5, then add 32
  */
    fahren =(9.0/5.0) * celsius + 32;

    printf("%.2fC is equal to %.2fF\n", celsius, fahren);
    
 getch();
 return 0;
}
