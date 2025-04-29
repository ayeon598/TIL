import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz11720 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		String[] input = br.readLine().split("");
		int sumNum = 0;
		for (int i = 0; i < n; i++) {
			int num = Integer.parseInt(input[i]);
			sumNum += num;
		}
		System.out.println(sumNum);
	}
}
