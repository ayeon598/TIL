import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Silver1436 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int cnt = 0;
		int num = 666;
		while(true) {
			if (String.valueOf(num).contains("666")) {
				cnt += 1;
			}
			if (cnt == N) {
				break;
			}
			num += 1;
		}
		System.out.println(num);
	}
}