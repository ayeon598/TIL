import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Silver1181 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		String[] words = new String[N];
		
		for (int i = 0; i < N; i++) {
			words[i] = br.readLine();
		}
		
		Arrays.sort(words, (a, b) -> {
			if (a.length() != b.length()) return a.length() - b.length();
			return a.compareTo(b);
		});
		
		String word = "";
		for (int i = 0; i < N; i++) {
			if (word.equals(words[i])) {
				continue;
			}
			bw.write(words[i]);
			bw.newLine();
			word = words[i];
		}
		bw.flush();
		bw.close();
	}
}
