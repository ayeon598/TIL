import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz24266 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		long n = Long.parseLong(br.readLine());
		System.out.println(n*n*n);
		System.out.println(3);
	}
}
