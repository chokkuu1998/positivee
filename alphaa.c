#include<ctype.h> 
#include<stdio.h> 
#include<conio.h> 
void main() 
{ 
char ch; 
for(;;){ 
ch = getc(stdin); 
if(ch == '.') break; 
if(isalnum(ch)) printf("%c is alphanumeric\n", ch); 
} 
getch(); 
} 
