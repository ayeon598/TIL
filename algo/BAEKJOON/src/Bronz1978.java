import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz1978 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        int res = 0;

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(input[i]);
            int cnt = 0;
            for (int j = 1; j <= num; j++) {
                if (num % j == 0) {
                    cnt += 1;
                }
                if (cnt > 2) {
                    break;
                }
            }
            if (cnt == 2) {
                res += 1;
            }
        }
        System.out.println(res);
    }
}
