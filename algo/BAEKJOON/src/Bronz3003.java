import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Bronz3003 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String[] input = br.readLine().split(" ");
		int[] num = {1, 1, 2, 2, 2, 8};
		for (int i = 0; i < input.length; i++) {
			int p = Integer.parseInt(input[i]);
			bw.write((num[i]-p)+" ");
		}
		bw.flush();
		bw.close();
	}
}
