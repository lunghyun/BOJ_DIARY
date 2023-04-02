import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        String output = "";
        while(true) {
            String T = br.readLine();
            if (T.charAt(0) == '0') {
                break;
            }
            for (int i = 0; i < T.length()-1-i; i++) {
                if (T.charAt(i) != T.charAt(T.length() - 1 - i)) {
                    T = T.concat("*");
                    output = output.concat("no\n");
                    break;
                }
            }
            if(T.charAt(T.length()-1) != '*'){
                output = output.concat("yes\n");
            }
        }
        System.out.print(output);
    }
}