import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        //String alphanumeric = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\\$%*+-./:"; // 왜이래

        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int R;
        String S;
        for(int i = 0; i < T; i++){
            R = sc.nextInt();
            S = sc.next();
            for(int j = 0; j < S.length(); j++) {
                for(int k = 0; k < R; k++){
                    System.out.print(S.charAt(j));
                }
            }
            System.out.print("\n");
        }
        sc.close();
    }
}