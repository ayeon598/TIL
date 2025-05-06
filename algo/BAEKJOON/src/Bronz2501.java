import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz2501 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int K = Integer.parseInt(input[1]);
        int cnt = 0;
        int res = 0;

        for (int i = 1; i <= N; i++) {
            if (N % i == 0) {
                cnt += 1;
            }
            if (cnt == K) {
                res = i;
                break;
            }
        }
        System.out.println(res);
    }
}
