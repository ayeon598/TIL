import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Silver2839 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int cnt = Integer.MAX_VALUE;
		int kilo5 = N / 5;
		for (int i = 0; i <= kilo5; i++) {
			int sugar = N - 5 * i;
			if (sugar % 3 == 0) {
				cnt = Math.min(cnt, i+sugar/3);
			}
		}
		if (cnt == Integer.MAX_VALUE) {
			System.out.println(-1);
		} else {
			System.out.println(cnt);
		}
	}
}
