import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz10810 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] arr = br.readLine().split(" ");
		int n = Integer.parseInt(arr[0]);
		int m = Integer.parseInt(arr[1]);
		int[] ball = new int[n];
		for (int a = 0; a < m; a++) {
			String[] input = br.readLine().split(" ");
			int i = Integer.parseInt(input[0]);
			int j = Integer.parseInt(input[1]);
			int k = Integer.parseInt(input[2]);
			for (int b = i; b <= j; b++) {
				ball[b-1] = k;
			}
		}
		StringBuilder sb = new StringBuilder();
		for (int a = 0; a < n; a++) {
			sb.append(ball[a]+" ");
		}
		System.out.println(sb);
	}
}
