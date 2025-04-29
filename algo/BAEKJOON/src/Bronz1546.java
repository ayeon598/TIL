import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz1546 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		String[] input = br.readLine().split(" ");
		int[] score = new int[n];
		float maxScore = Integer.MIN_VALUE;
		for (int i = 0; i < n; i++) {
			int num = Integer.parseInt(input[i]);
			score[i] = num;
			if (maxScore < num) {
				maxScore = num;
			}
		}
		float sumScore = 0;
		for (int i = 0; i < n; i++) {
			float newScore = score[i]/maxScore*100;
			sumScore += newScore;
		}
		float avg = sumScore/n;
		System.out.println(avg);
	}
}
