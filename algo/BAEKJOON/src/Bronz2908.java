import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz2908 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] input = br.readLine().split(" ");
		int a = Integer.parseInt(input[0]);
		int b = Integer.parseInt(input[1]);
		int c = a/100 + ((a/10)%10)*10 + (a%10)*100;
		int d = b/100 + ((b/10)%10)*10 + (b%10)*100;
		int max = Math.max(c, d);
		System.out.println(max);
	}
}
