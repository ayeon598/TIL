import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz15894 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		long n = Integer.parseInt(br.readLine());
		System.out.println(4*n);
	}
}
