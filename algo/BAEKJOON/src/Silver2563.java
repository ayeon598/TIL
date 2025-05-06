import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Silver2563 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        boolean[][] paper = new boolean[100][100];
        int N = Integer.parseInt(br.readLine());
        int area = 0;

        for (int n = 0; n < N; n++) {
            String[] input = br.readLine().split(" ");
            int x = Integer.parseInt(input[0]);
            int y = Integer.parseInt(input[1]);

            for (int i = x; i < x + 10; i++) {
                for (int j = y; j < y + 10; j++) {
                    if (!paper[i][j]) {
                        paper[i][j] = true;
                        area++;
                    }
                }
            }
        }
        System.out.println(area);
    }
}
