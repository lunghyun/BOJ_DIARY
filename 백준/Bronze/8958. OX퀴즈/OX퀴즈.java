import java.util.Scanner;
public class Main {
    //자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        String sumstr = "";
        for(int i = 0; i < T; i++){
            String str = sc.next();
            int temp = 1;
            int sum = 0;
            for(int j = 0; j < str.length(); j++){
                if(str.charAt(j) == 'O'){
                    if(j == 0){
                        sum += temp;
                    }
                    else if(str.charAt(j-1) == str.charAt(j)){
                        temp += 1;
                        sum += temp;
                    }
                    else{
                        sum += temp;
                    }
                }
                else if(str.charAt(j) == 'X'){
                    temp = 1;
                }
            }
            sumstr = sumstr.concat(Integer.toString(sum));
            sumstr = sumstr.concat("\n");
        }
        System.out.print(sumstr);
        sc.close();
    }
}