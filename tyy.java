import java.util.*;
class Num
{
    void main()
    {
        Scanner sc=new Scanner(System.in);
        int n1=0, n2=0, n3=0; 
        int small= 999, large= -999; 
 
        // Taking inputs using Scanner class
 
        System.out.println("Enter 1st number");
        n1=sc.nextInt();
        System.out.println("Enter 2nd number");
        n2=sc.nextInt();
        System.out.println("Enter 3rd number");
        n3=sc.nextInt();
 
      
 
        if(n1==n2 && n2==n3 && n3==n1)
 
            System.out.println("Error! Numbers are equal");
 
        else
        {
 
         
            if( n1==n2) n1= -99; 
            if(n2==n3) n2= -99;
            if(n3==n1) n3= -99;
  equality or repetition of numbers is eliminated from the code by the help of the'not equal to' (!=) condition */
 
            if(n1!=-99) 
            {
                if(n1> large)  
                    large=n1;
 
                if( n1<small)
                    small=n1;
            }
 
          ame for n3.
 
            if(n2!=-99) 
            {
                if(n2> large) 
                    large=n2;
 
                if( n2<small)
                    small=n2;
 
            }
            if(n3!=-99) 
            {
                if(n3> large)
                    large=n3;
 
                if( n3<small)
                    small=n3;
 
            }
 
                
            System.out.println (" Largest number : "+ large);
            System.out.println (" Smallest number : "+ small);
        }
    }
}
