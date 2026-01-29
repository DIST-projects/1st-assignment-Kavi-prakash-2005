import java.rmi.Remote;
import java.rmi.RemoteException;

/*
 * Remote interface
 * Declares methods that can be called remotely by the client
 */
public interface TextService extends Remote {

    // Counts number of words in the given text
    int wordCount(String text) throws RemoteException;

    // Reverses the given text
    String reverseText(String text) throws RemoteException;

    // Checks if the given text is a palindrome
    boolean isPalindrome(String text) throws RemoteException;
}
