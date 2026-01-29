import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;

/*
 * Implements the remote interface
 * Contains actual logic executed on the server
 */
public class TextServiceImpl extends UnicastRemoteObject implements TextService {

    // Mandatory constructor (throws RemoteException)
    protected TextServiceImpl() throws RemoteException {
        super();
    }

    @Override
    public int wordCount(String text) throws RemoteException {
        return text.split("\\s+").length;
    }

    @Override
    public String reverseText(String text) throws RemoteException {
        return new StringBuilder(text).reverse().toString();
    }

    @Override
    public boolean isPalindrome(String text) throws RemoteException {
        String clean = text.replaceAll("\\s+", "").toLowerCase();
        return clean.equals(new StringBuilder(clean).reverse().toString());
    }
}
