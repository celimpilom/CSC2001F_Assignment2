import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.List;

/**
* Class to run AVL tree 
*
* @author Celimpilo Manqele
* @version 1.0
*/
public class AccessAVLApp {

    static AVLTree<String>   tree;
    static int index;
    static List<String> slist;
    public static void main(String[] args ) throws FileNotFoundException{
        String filename = (args.length <= 1) ? "oklist.txt" : args[1];
        ReadFile object = new ReadFile(filename);
        tree = object.getTree();
        object.tree();
        slist = Arrays.asList(object.slist);
        
        if (args.length >= 1){
            String studentID = args[0];
            System.out.println(printStudent(studentID));
            System.out.println("insertcount is \n" + object.iCountList[index]);
            System.out.println("opcount is \n" + tree.opCount);
        } else {
            printAll();
 
        }
          
    }
    static String printStudent(String studentID){
        /**
    * Method to print stundent name and surname given the student number
    *
    * @param studentID the student number of a student
    */
        BinaryTreeNode<String> foundNode = tree.find(studentID);
            if (foundNode != null){
                index = slist.indexOf(foundNode.data);
                String[] b = foundNode.data.split(" ");
                return b[1] + " " + b[2];
            }
           
        return "Access denied!";
            } 
    
    /**
    * Method to print all students
    */
    static void printAll(){
        tree.treeOrder();
    }
}

    

