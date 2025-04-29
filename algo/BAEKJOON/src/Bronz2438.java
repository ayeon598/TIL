import java.io.*;

public class Bronz2438 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		for (int i = 1; i <= n; i++) {
			bw.write("*".repeat(i));
			bw.newLine();
		}
		bw.flush();
		bw.close();
	}
}
