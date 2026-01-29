import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

/*
 * Starts RMI registry and binds the remote object
 */
public class RMIServer {

    public static void main(String[] args) {
        try {
            // Start RMI Registry on default port 1099
            LocateRegistry.createRegistry(1099);

            // Create remote object
            TextService service = new TextServiceImpl();

            // Bind object to RMI registry
            Naming.rebind("rmi://0.0.0.0/TextService", service);

            System.out.println("✅ RMI Server is running on port 1099");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
