import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz2869 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int A = Integer.parseInt(input[0]);
        int B = Integer.parseInt(input[1]);
        int V = Integer.parseInt(input[2]);
        int day = (V-B-1) / (A-B) + 1;
        System.out.println(day);
    }
}
