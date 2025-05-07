import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Silver24313 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] input = br.readLine().split(" ");
		int a1 = Integer.parseInt(input[0]);
		int a0 = Integer.parseInt(input[1]);
		int c = Integer.parseInt(br.readLine());
		int n0 = Integer.parseInt(br.readLine());
		
		int f = a1*n0 + a0;
		int g = c * n0;
		if (f <= g && a1 <= c) {
			System.out.println(1);
		} else {
			System.out.println(0);
		}
	}
}
