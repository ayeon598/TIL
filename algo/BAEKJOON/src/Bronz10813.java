import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz10813 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] arr = br.readLine().split(" ");
		int n = Integer.parseInt(arr[0]);
		int m = Integer.parseInt(arr[1]);
		int[] ball = new int[n];
		for (int i = 0; i < n; i++) {
			ball[i] = i+1;
		}
		for (int a = 0; a < m; a++) {
			String[] input = br.readLine().split(" ");
			int i = Integer.parseInt(input[0]);
			int j = Integer.parseInt(input[1]);
			
			int num = ball[i-1];
			ball[i-1] = ball[j-1];
			ball[j-1] = num;
		}
		StringBuilder sb = new StringBuilder();
		for (int a = 0; a < n; a++) {
			sb.append(ball[a]+" ");
		}
		System.out.println(sb);
	}
}
