import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Silver10814 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		String[][] members = new String[N][3];
		
		for (int i = 0; i < N; i++) {
			String[] input = br.readLine().split(" ");
			members[i][0] = input[0];
			members[i][1] = input[1];
			members[i][2] = String.valueOf(i);
		}
		
		Arrays.sort(members, (a, b) -> {
			if (Integer.parseInt(a[0]) != Integer.parseInt(b[0])) return Integer.parseInt(a[0]) - Integer.parseInt(b[0]);
			return Integer.parseInt(a[2]) - Integer.parseInt(b[2]);			
		});
		
		for (int i = 0; i < N; i++) {
			bw.write(members[i][0] + " " + members[i][1]);
			bw.newLine();
		}
		bw.flush();
		bw.close();
	}
}
