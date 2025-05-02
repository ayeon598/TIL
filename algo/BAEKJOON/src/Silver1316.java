import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Silver1316 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		int cnt = 0;
		for (int i = 0; i < t; i++) {
			String[] input = br.readLine().split("");
			String alpha = "";
			String lastAlpha = "";
			boolean group = true;
			for (int j = 0; j < input.length; j++) {
				if (alpha.contains(input[j])) {
					if (!lastAlpha.equals(input[j])) {
						group = false;
						break;
					}
				} else {
					alpha += input[j];
					lastAlpha = input[j];
				}
			}
			if (group) {
				cnt += 1;
			}
		}
		System.out.println(cnt);
	}
}
