import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz24267 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		long n = Long.parseLong(br.readLine());
		long res = n * (n-1) * (n-2) / 6;
		System.out.println(res);
		System.out.println(3);
	}
}
