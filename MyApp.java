import java.util.logging.*;

public class MyApp {
    private static final Logger logger = Logger.getLogger(MyApp.class.getName());

    public static void main(String[] args) {
        logger.info("Application started");
        try {
            int result = 10 / 0;
        } catch (ArithmeticException e) {
            logger.severe("Error: " + e.getMessage());
        }
        logger.info("Application ended");
    }
}
