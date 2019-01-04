public static long extractOddDigits(long n){


String output = "";
if(n < 0) // check if negative
{   
    output = "Error Input!!";

}
if(n % 2 == 0){ 

    output = "-1";
}

while(n > 0) { 
   int left = (int) (n % 10);
   if(left % 2 != 0)    
     output = left + output;
     n /= 10;
}
System.out.println("oddDigit = " + output);
 }
