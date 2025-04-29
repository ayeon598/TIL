import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Bronz10807 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		String[] arr = br.readLine().split(" ");
		int v = Integer.parseInt(br.readLine());
		int cnt = 0;
		
		for (int i = 0; i < arr.length; i++) {
			int num = Integer.parseInt(arr[i]);
			if (num == v) {
				cnt += 1;
			}
		}
		System.out.println(cnt);
	}
}
