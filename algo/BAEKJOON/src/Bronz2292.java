import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz2292 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int layer = 1; // 시작은 1번 방
        int maxRoom = 1;

        while (N > maxRoom) {
            maxRoom += 6 * layer;
            layer++;
        }

        System.out.println(layer);
    }
}
