import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Bronz2444 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int input = Integer.parseInt(br.readLine());
		for (int i = 1; i <= input; i++) {
			bw.write(" ".repeat(input-i)+"*".repeat(2*i-1));
			bw.newLine();
		}
		for (int i = input-1; i > 0; i--) {
			bw.write(" ".repeat(input-i)+"*".repeat(2*i-1));
			bw.newLine();
		}
		bw.flush();
		bw.close();
	}
}
