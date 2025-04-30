import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz1157 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String input = br.readLine();
		int[] cnt = new int[26];
		char start = 'A';
		for (int i = 0; i < input.length(); i++) {
			char ch = input.charAt(i);
			int alpha = (int)ch - (int)start;
			if (alpha > 31) {
				alpha -= 32;
			}
			cnt[alpha] += 1;
		}
		String result = "";
		int maxCnt = Integer.MIN_VALUE;
		for (int i = 0; i < cnt.length; i++) {
			maxCnt = Math.max(maxCnt, cnt[i]);
		}
		for (int i = 0; i < cnt.length; i++) {
			if (cnt[i] == maxCnt) {
				result += (char)(i+65);
			}
		}
		if (result.length() == 1) {
			System.out.println(result);
		} else {
			System.out.println("?");
		}
	}
}
