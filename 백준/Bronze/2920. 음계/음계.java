import java.util.Scanner;
public class Main {
    //자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        str = str.replaceAll(" ", "");

        if(str.equals("12345678"))
            System.out.println("ascending");
        else if (str.equals("87654321"))
            System.out.println("descending");
        else
            System.out.println("mixed");
        sc.close();
    }
}