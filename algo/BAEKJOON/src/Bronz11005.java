import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz11005 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int B = Integer.parseInt(input[1]);

        String res = Integer.toString(N, B).toUpperCase();
        System.out.println(res);
    }
}
