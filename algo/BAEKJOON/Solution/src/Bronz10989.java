import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Bronz10989 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		int[] count = new int[10001];
		
		for (int i = 0; i < N; i++) {
			int num = Integer.parseInt(br.readLine());
			count[num] += 1;
		}
		
		for (int i = 0; i < count.length; i++) {
			while (count[i] > 0) {
				bw.write(i + "");
				bw.newLine();
				count[i] -= 1;
			}
		}
		bw.flush();
		bw.close();
	}
}
