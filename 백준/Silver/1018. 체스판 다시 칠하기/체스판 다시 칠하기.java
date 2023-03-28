import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static boolean[][] arr;
    public static int min = 64;
    public static void Chess(int a, int b){
        boolean temp = arr[a][b];
        int count = 0;
        for(int i = a; i < a+8; i++){
            for(int j = b; j < b+8; j++){
                if(temp != arr[i][j]){
                    count++;
                }
                temp = !temp;
            }
            temp = !temp;
        }

        count = Math.min(count, 64-count);
        min = Math.min(min, count);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int T = Integer.parseInt(st.nextToken());
        int J = Integer.parseInt(st.nextToken());

        arr = new boolean[T][J];

        for(int i = 0; i < T; i++){
            String str = br.readLine();
            for(int j = 0; j < J; j++){
                if(str.charAt(j) == 'B'){
                    arr[i][j] = true;
                }
                else if (str.charAt(j) == 'W') {
                    arr[i][j] = false;
                }
            }
        }

        for(int i = 0; i < T-7; i++){ // 첫번째 칸이 w or b 이 되므로 count or 64-count 중 작은 것을 출력한다
            for(int j = 0; j < J-7; j++){
                Chess(i, j);
            }
        }
        System.out.print(min);
    }
}