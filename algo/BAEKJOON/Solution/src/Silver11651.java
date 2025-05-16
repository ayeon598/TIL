import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Silver11651 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		Integer[][] dots = new Integer[N][2];
		
		for (int i = 0; i < N; i++) {
			String[] input = br.readLine().split(" ");
			dots[i][0] = Integer.parseInt(input[0]);
			dots[i][1] = Integer.parseInt(input[1]);
		}
		
		Arrays.sort(dots, (a, b) -> {
			if (!a[1].equals(b[1])) return a[1] - b[1];
			return a[0] - b[0];
		});
		
		for (int i = 0; i < N; i++) {
			bw.write(dots[i][0] + " " + dots[i][1]);
			bw.newLine();
		}
		bw.flush();
		bw.close();
	}
}
