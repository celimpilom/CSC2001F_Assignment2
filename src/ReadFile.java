/**
*helper class to readfiles
*
* @author Celimpilo Manqele
* @version 1.0
*/
import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files

public class ReadFile {
    File myObj;
    Scanner myReader;
    String[] slist;
    AVLTree<String> tree;
    int[] iCountList;

    ReadFile(String filename) throws FileNotFoundException{
        myObj = new File("files/" + filename);
        myReader = new Scanner(myObj);
        slist = new String[5000];
        tree = new AVLTree<String>();
        iCountList = new int[5000];
        }
    
    void tree(){
        int i = 0;
        while (myReader.hasNextLine()) {
          String data = myReader.nextLine();
          tree.insert(data.toString());
          slist[i] = data.toString();
          iCountList[i] = tree.insertcount;
          i++;
        } 
    }


    public AVLTree<String> getTree(){
        return this.tree;//returns AVL tree
    }

}