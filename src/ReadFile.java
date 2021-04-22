import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files

public class ReadFile {
    File myObj;
    Scanner myReader;
    String[] list;
    AVLTree<String> tree;
    
    ReadFile() throws FileNotFoundException{
        myObj = new File("files/oklist.txt");
        myReader = new Scanner(myObj);
        list = new String[5000];
        tree = new AVLTree<String>();
    }

    void array() throws FileNotFoundException {
        int counter = 0;
          while (myReader.hasNextLine()) {
            String data = myReader.nextLine();
            list[counter] = data.toString();
            counter++;
        }       
          myReader.close();
    }

    void tree(){
        while (myReader.hasNextLine()) {
          String data = myReader.nextLine();
          tree.insert(data.toString());
    
      }              // Creates BST
    }
    public AVLTree<String> getTree(){
        return this.tree;//returns Tree
    }

    public String[] getArray(){
        return list;
    }
    
}