import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz2566 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int max = Integer.MIN_VALUE;
		int maxi = 0;
		int maxj = 0;
		for (int i = 0; i < 9; i++) {
			String[] line = br.readLine().split(" ");
			for (int j = 0; j < line.length; j++) {
				int num = Integer.parseInt(line[j]);
				if (num > max) {
					max = num;
					maxi = i+1;
					maxj = j+1;
				}
			}
		}
		System.out.println(max);
		System.out.println(maxi + " " + maxj);
	}
}
