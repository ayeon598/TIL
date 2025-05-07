import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz24265 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		long n = Long.parseLong(br.readLine());
		long res = 0;
		for (int i = 1; i < n; i++) {
			res += n-i;
		}
		System.out.println(res);
		System.out.println(2);
	}
}
