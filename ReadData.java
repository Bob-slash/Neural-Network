
import java.util.*;
import java.io.*;

public class ReadData
{
    String file = "train.csv";
    double[][] inputs = {{0.1, 0.2, 0.7},{1.9, 0.6, 0.3}};
    int[] label = {0,1};
    public ReadData()
    {
       //readFromFile()//
    }

    public double[][] readFromFile(){

        try{ 
            BufferedReader fh = new BufferedReader(new FileReader(file));//opens the file
            String s;

            int counter=0;
          
            s=fh.readLine();
           // while (  (s=fh.readLine())!=null){ //loops keeps going until there are no more lines to read
            while (counter < 100){
               
             
            	 s=fh.readLine();
                 //System.out.println("Line " + counter + " " + s);
            	 String[] vals = s.split(",");
            	 for(int i = 0; i < inputs[counter].length; i++) {
            		 inputs[counter][i] = Double.parseDouble(vals[i + 1]);
            	 }
            	 label[counter] = Integer.parseInt(vals[0]);
                
                counter++;
                
            }//end of while

            for(int i = 0; i < label.length; i++) {
            	System.out.println(label[i]);
            }
            System.out.println("------------------");
            
            fh.close(); //close the file

        } catch (Exception e){ //if there was an error in accessing the file this would catch it.
            System.out.println("There was an error"); 
        }
        
      
        return inputs;

    }//end of readFromFile Method

}
