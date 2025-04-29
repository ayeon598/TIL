import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz10811 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] arr = br.readLine().split(" ");
		int n = Integer.parseInt(arr[0]);
		int m = Integer.parseInt(arr[1]);
		
		int[] basket = new int[n];
		for (int a = 0; a < n; a++) {
			basket[a] = a+1;
		}
		for (int a = 0; a < m; a++) {
			String[] input = br.readLine().split(" ");
			int i = Integer.parseInt(input[0]);
			int j = Integer.parseInt(input[1]);
			while(i != j) {
				int num = basket[i-1];
				basket[i-1] = basket[j-1];
				basket[j-1] = num;
				if (i+1 == j) {
					break;
				}
				i += 1;
				j -= 1;
			}
		}
		StringBuilder sb = new StringBuilder();
		for (int a = 0; a < n; a++) {
			sb.append(basket[a]+" ");
		}
		System.out.println(sb);
	}
}
