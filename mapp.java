import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class DuplicateWords 
{
    
    public static void main(String[] args) 
    {
        System.out.print("Enter string to analyse:");
        Scanner sn = new Scanner(System.in);
        String input = sn.nextLine();
        
 
        String[] words = input.split(" ");
        
      
        Map<String,String> wordMap = new HashMap<String,String>();
        for(int i=0;i<words.length;i++)
        {
            String word = words[i].toUpperCase(); 
            if(wordMap.get(word)!=null)
            {
                          System.out.println("Duplicated/Repeated word:"+word);
            }
            else 
            {
                wordMap.put(word, word);
            }
        }
    }   
}
