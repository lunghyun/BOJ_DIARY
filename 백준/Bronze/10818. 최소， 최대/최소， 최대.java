import java.util.Arrays;
import java.util.Scanner;

public class Main {
    //자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int[] arr = new int[T];
        int max, min = 0;
        String sumstr = "";
        for(int i = 0; i < T; i++){
            arr[i] = sc.nextInt();
        }
        System.out.print(Arrays.stream(arr).min().getAsInt());
        System.out.print(" ");
        System.out.print(Arrays.stream(arr).max().getAsInt());
        sc.close();
    }
}