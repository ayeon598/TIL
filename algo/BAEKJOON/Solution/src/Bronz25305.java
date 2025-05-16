import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Bronz25305 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] input = br.readLine().split(" ");
		int N = Integer.parseInt(input[0]);
		int k = Integer.parseInt(input[1]);
		int[] numbers = new int[N];
		String[] nums = br.readLine().split(" ");
		
		for (int i = 0; i < N; i++) {
			numbers[i] = Integer.parseInt(nums[i]);
		}
		Arrays.sort(numbers);
		System.out.println(numbers[N-k]);
	}
}
