import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Silver2941 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = "";
		int cnt = 0;
		String[] arr = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
		String firstAlpha = "cdlnsz";
		String[] input = br.readLine().split("");
		for (int i = 0; i < input.length; i++) {
			if (str == "") {
				if (firstAlpha.contains(input[i])) {
					str += input[i];
				} else {
					cnt += 1;
				}
			} else if (str.length() == 1) {
				str += input[i];
				for (int j = 0; j < arr.length; j++) {
					if (str.equals(arr[j])) {
						cnt += 1;
						str = "";
						break;
					}
				}
				if (str != "" && !str.equals("dz")) {
					cnt += 1;
					String newStr = str.substring(1);
					str = newStr;
				}
			} else {
				if (input[i].equals("=")) {
					cnt += 1;
					str = "";
				} else {
					cnt += 2;
					str = input[i];
				}
			}
		}
		if (str != "") {
			cnt += str.length();
		}
		System.out.println(cnt);
	}
}
