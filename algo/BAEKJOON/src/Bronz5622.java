import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz5622 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] input = br.readLine().split("");
		String num2 = "ABC";
		String num3 = "DEF";
		String num4 = "GHI";
		String num5 = "JKL";
		String num6 = "MNO";
		String num7 = "PQRS";
		String num8 = "TUV";
		String num9 = "WXYZ";
		
		int time = 0;
		for (int i = 0; i < input.length; i++) {
			if (num2.contains(input[i])) {
				time += 3;
			} else if (num3.contains(input[i])) {
				time += 4;
			} else if (num4.contains(input[i])) {
				time += 5;
			} else if (num5.contains(input[i])) {
				time += 6;
			} else if (num6.contains(input[i])) {
				time += 7;
			} else if (num7.contains(input[i])) {
				time += 8;
			} else if (num8.contains(input[i])) {
				time += 9;
			} else if (num9.contains(input[i])) {
				time += 10;
			}
		}
		System.out.println(time);

	}
}
