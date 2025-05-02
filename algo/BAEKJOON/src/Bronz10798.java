import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Bronz10798 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String[] input = new String[5];
		int[] length = new int[5];
		int max = Integer.MIN_VALUE;
		String res = "";
		for (int i = 0; i < 5; i++) {
			input[i] = br.readLine();
			length[i] = input[i].length();
			max = Math.max(max, length[i]);
		}
		for (int i = 0; i < max; i++) {
			for (int j = 0; j < 5; j++) {
				if (i < length[j]) {
					bw.write(input[j].charAt(i));
				}
			}
		}
		bw.flush();
		bw.close();
	}
}
