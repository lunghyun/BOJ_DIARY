import java.util.Scanner;
import java.lang.Math;
public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int x1, x2 ,y1, y2, r1, r2;
        int[] temp = new int[T];
        for(int i = 0; i < T; i++) {
            x1 = sc.nextInt();
            y1 = sc.nextInt();
            r1 = sc.nextInt();
            x2 = sc.nextInt();
            y2 = sc.nextInt();
            r2 = sc.nextInt();
            double r = Math.sqrt(Math.pow((x1-x2), 2.0) + Math.pow((y1-y2), 2.0));
            if(x1==x2 &&    //무한대
            y1 == y2 &&
            r1 == r2){
                temp[i] = -1;
            }
            else if(Math.max(r1, r2) < r){ //외접
                if(r < r1 + r2){
                    temp[i] = 2;
                }
                else if(r > r1 + r2){
                    temp[i] = 0;
                }
                else{
                    temp[i] = 1;
                }
            }
            else if(Math.max(r1, r2) > r){ //내접
                if(r < Math.abs(r1 - r2)){
                    temp[i] = 0;
                }
                else if(r > Math.abs(r1 - r2)){
                    temp[i] = 2;
                }
                else {
                    temp[i] = 1;
                }
            }
            else {
                temp[i] = 2;
            }
        }
        for(int i = 0; i < T; i++) {
            System.out.println(temp[i]);
        }
        sc.close();
    }
}