import java.util.Scanner;
import java.lang.Math;
public class Main {
    //자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while(T > 0){
            System.out.println(T);
            T--;
        }
        sc.close();
    }
}