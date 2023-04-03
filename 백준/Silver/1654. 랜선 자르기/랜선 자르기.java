import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int k = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        List<Integer> lanCables = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            lanCables.add(Integer.parseInt(br.readLine()));
        }

        Collections.sort(lanCables); // sort the array to apply binary search

        long left = 1;
        long right = lanCables.get(k - 1); // maximum possible length of LAN cable

        while (left <= right) {
            long mid = (left + right) / 2;
            long count = 0;

            for (int i = 0; i < k; i++) {
                count += lanCables.get(i) / mid;
            }

            if (count >= n) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        System.out.println(right); // print the maximum length of LAN cable
    }
}
