import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Bronz2587 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] numbers = new int[5];
		int sum = 0;
		
		for (int i = 0; i < 5; i++) {
			int num = Integer.parseInt(br.readLine());
			numbers[i] = num;
			sum += num;
		}
		Arrays.sort(numbers);
		System.out.println(sum/5);
		System.out.println(numbers[2]);
	}
}
