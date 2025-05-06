import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz2581 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int M = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());
        int min = -1;
        int sumN = 0;

        for (int i = M; i <= N; i++) {
            int cnt = 0;
            for (int j = 1; j <= i; j++) {
                if (i % j == 0) {
                    cnt += 1;
                }
                if (cnt > 2) {
                    break;
                }
            }
            if (cnt == 2) {
                sumN += i;
                if (min == -1) {
                    min = i;
                }
            }
        }
        if (min == -1) {
            System.out.println(-1);
        } else {
            System.out.println(sumN);
            System.out.println(min);
        }
    }
}
