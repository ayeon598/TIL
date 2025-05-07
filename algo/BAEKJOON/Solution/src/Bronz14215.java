import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Bronz14215 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] input = br.readLine().split(" ");
		int line1 = Integer.parseInt(input[0]);
		int line2 = Integer.parseInt(input[1]);
		int line3 = Integer.parseInt(input[2]);
		int[] line = {line1, line2, line3};
		Arrays.sort(line);
		
		if (line[2] < line[0] + line[1]) {
			System.out.println(line1+line2+line3);
		} else {
			while (line[2] >= line[0] + line[1]) {
				line[2] -= 1;
			}
			System.out.println(line[0]+line[1]+line[2]);
		}
	}
}
