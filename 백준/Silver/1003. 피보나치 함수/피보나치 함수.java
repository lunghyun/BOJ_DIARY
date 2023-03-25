import java.util.Scanner;
import java.lang.Math;
public class Main {
    static int num0, num1;
    static int temp;
    public static void fibonacci(int n){
        num0 = 1;
        num1 = 0;
        temp = num0;
        for(int i = 0; i< n; i++){
            num0 = num1;
            num1 = temp;
            temp = num0 + num1;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int[] num = new int[T];
        for(int i = 0; i < T; i++) {
            num[i] = sc.nextInt();
        }
        for(int i = 0; i < T; i++) {
            fibonacci(num[i]);
            System.out.print(num0);
            System.out.print(" ");
            System.out.println(num1);
        }
        sc.close();
    }
}