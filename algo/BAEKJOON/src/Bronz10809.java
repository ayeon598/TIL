import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz10809 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str = br.readLine();
		int[] loc = new int[26];
		char a = 'a';
		for (int i = 0; i < loc.length; i++) {
			loc[i] = -1;
		}
		for (int i = 0; i < str.length(); i++) {
			char ch = str.charAt(i);
			int num = (int)ch - (int)a;
			if (loc[num] == -1) {
				loc[num] = i;
			}
		}
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < loc.length; i++) {
			sb.append(loc[i]+" ");
		}
		System.out.println(sb);
	}
}
