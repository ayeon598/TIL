import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Collections;

public class Bronz5073 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int line1 = -1;
		int line2 = -1;
		int line3 = -1;
		
		while (line1 != 0) {
			String[] input = br.readLine().split(" ");
			line1 = Integer.parseInt(input[0]);
			line2 = Integer.parseInt(input[1]);
			line3 = Integer.parseInt(input[2]);
			int[] line = {line1, line2, line3};
			Arrays.sort(line);
			if (line1 == 0) {
				break;
			}
			if (line[2] >= line[0] + line[1]) {
				bw.write("Invalid");
				bw.newLine();
			} else if (line1 == line2 && line2 == line3) {
				bw.write("Equilateral");
				bw.newLine();
			} else if (line1 == line2 || line2 == line3 || line3 == line1) {
				bw.write("Isosceles");
				bw.newLine();
			} else {
				bw.write("Scalene");
				bw.newLine();
			}	
		}
		bw.flush();
		bw.close();
	}
}
