import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Silver1193 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int X = Integer.parseInt(br.readLine());

        int line = 1;
        int cnt = 0;

        while (X > cnt + line) {
            cnt += line;
            line++;
        }

        int x = X - cnt;

        int num1 = 0;
        int num2 = 0;
        if (line % 2 == 0) {
            num1 = x;
            num2 = line - x + 1;
        } else {
            num1 = line - x + 1;
            num2 = x;
        }

        System.out.println(num1 + "/" + num2);
    }
}
