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
        int T = Integer.parseInt(br.readLine());
        String[] str = new String[T];

        for(int i = 0; i < T; i++){
            str[i] = br.readLine();
        }
        Arrays.sort(str, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                if(s1.length() == s2.length()){
                    return s1.compareTo(s2);
                }
                else{
                    return s1.length() - s2.length();
                }
            }
        });

        System.out.println(str[0]);
        for(int i = 1; i < T; i++){
            if(!str[i].equals(str[i-1])){
                System.out.println(str[i]);
            }
        }
    }
}