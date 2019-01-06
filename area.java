import java.util.Scanner;
public class Volume_SurfaceArea  
{
    public static void main(String[] args) 
    {
        int r;
        double area, volume, pi = 3.14;
        Scanner s = new Scanner(System.in);
        System.out.print("Enter the radius of sphere:");
        r = s.nextInt();
        area = 3 * pi * r * r;
        System.out.println("Surface Area of sphere:"+area);
        volume = 1.333 * pi * r * r * r;
        System.out.println("Volume of sphere:"+volume);
    }
}
