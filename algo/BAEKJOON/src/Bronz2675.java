import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Bronz2675 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int t = Integer.parseInt(br.readLine());
		for (int i = 0; i < t; i++) {
			String[] input = br.readLine().split(" ");
			int cnt = Integer.parseInt(input[0]);
			String str = input[1];
			for (int j = 0; j < str.length(); j++) {
				bw.write(str.substring(j,j+1).repeat(cnt));
			}
			bw.newLine();
		}
		bw.flush();
		bw.close();
	}
}
