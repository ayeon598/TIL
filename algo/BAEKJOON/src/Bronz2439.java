import java.io.*;

public class Bronz2439 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		for (int i = 1; i <= n; i++) {
			String res = "*".repeat(i);
			String blank = " ".repeat(n-res.length());
			bw.write(blank+res);
			bw.newLine();			
		}
		bw.flush();
		bw.close();
	}
}
