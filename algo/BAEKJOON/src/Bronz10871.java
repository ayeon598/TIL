import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Bronz10871 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String[] input = br.readLine().split(" ");
		int n = Integer.parseInt(input[0]);
		int x = Integer.parseInt(input[1]);
		String[] arr = br.readLine().split(" ");
		for (int i = 0; i < n; i++) {
			int num = Integer.parseInt(arr[i]);
			if (num < x) {
				bw.write(num+" ");
			}
		}
		bw.flush();
		bw.close();
	}
}
