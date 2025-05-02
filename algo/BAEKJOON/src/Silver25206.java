import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Silver25206 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] input;
		String line;
		String[] str = {"A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"};
		double[] score = {4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0};
		double sumScore = 0.0;
		double sumSubject = 0.0;
//		for (int j = 0; j < 20; j++) {
//			input = br.readLine().split(" ");
		while ((line = br.readLine()) != null) {
			input = line.split(" ");
			if (input[2].equals("P")) {
				continue;
			}
			double subject = Double.parseDouble(input[1]);
			for (int i = 0; i < str.length; i++) {
				if (input[2].equals(str[i])) {
					sumScore += score[i]*subject;
					sumSubject += subject;
					break;
				}
			}
		}
		double res = 0.0;
		if (sumSubject != 0.0) {
			res = sumScore/sumSubject;
		}
		System.out.println(res);
	}
}
