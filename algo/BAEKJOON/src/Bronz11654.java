import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz11654 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str = br.readLine();
		char ch = str.charAt(0);
		int ascii = (int)ch;
		System.out.println(ascii);
	}
}
