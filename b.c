#include <iostream> 
using namespace std; 
 void findMultiples(int n)  
{  
int a = 3; // To keep track of multiples of 3  
int b = 5; // To keep track of multiples of 5  
for (int i = 1; i <= n; i++)  
 {  
   string s = "";  
  
  if (i == a)  
        {  
            a = a + 3; 
            s = s + "Multiple of 3. ";  
        }  
  
        if (i == b)  
        {  
            b = b + 5; 
            s = s + "Multiple of 5.";  
        }  
  
        if (s == "")  
            cout << (i) << endl;  
        else
        cout << (s) << endl;  
    }  
}  
  

int main()  
{ 
    findMultiples(20);  
  
    return 0; 
} 
