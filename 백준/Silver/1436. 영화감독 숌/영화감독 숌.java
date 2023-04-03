import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int num = 665;
        int T = Integer.parseInt(br.readLine());

        for(int i = 0; i < T; i++){
            num++;
            if(!String.valueOf(num).contains("666")) {
                i--;
            }
        }
        System.out.println(num);
    }
}