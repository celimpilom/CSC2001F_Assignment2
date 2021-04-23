/**
* Class to run AVL tree 
*
* @author Celimpilo Manqele
* @version 1.0
*/
import java.io.FileNotFoundException;

public class AccessAVLApp {

    static AVLTree<String>   tree;
    public static void main(String[] args ) throws FileNotFoundException{

        ReadFile object = new ReadFile();
        tree = object.getTree();
        
        if (args.length == 1){
            String studentID = args[0];
            System.out.println(printStudent(studentID)  );
            System.out.println(tree.opCount);
        } else {
            printAll();
 
        }
          
    }
    static String printStudent(String studentID){
        BinaryTreeNode<String> foundNode = tree.find(studentID);
            if (foundNode != null){
                String[] b = foundNode.data.split(" ");
                return b[1] + " " + b[2];
            }
           
        return "Access denied!";
            } 
    static void printAll(){
        tree.treeOrder();
    }
}

    

