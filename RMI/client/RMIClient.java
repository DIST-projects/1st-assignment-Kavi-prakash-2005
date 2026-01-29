import java.rmi.Naming;

/*
 * Client program that accesses remote methods
 */
public class RMIClient {

    public static void main(String[] args) {
        try {
            // Replace with your Azure VM Public IP
            String serverIP = "rmi://52.237.81.179/TextService";

            // Lookup remote object
            TextService service = (TextService) Naming.lookup(serverIP);

            String text = "Never odd or even";

            // Remote method calls
            System.out.println("Word Count: " + service.wordCount(text));
            System.out.println("Reversed Text: " + service.reverseText(text));
            System.out.println("Is Palindrome: " + service.isPalindrome(text));

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
