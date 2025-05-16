import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Silver18870 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		String[] input = br.readLine().split(" ");
		int[] numbers = new int[N];
		Set<Integer> nums = new HashSet<>();

		for (int i = 0; i < N; i++) {
			numbers[i] = Integer.parseInt(input[i]);
			nums.add(numbers[i]);
		}
		
		List<Integer> list = new ArrayList<>(nums);
		Collections.sort(list);
		
		Map<Integer, Integer> map = new HashMap<>();
		for (int i = 0; i < list.size(); i++) {
			map.put(list.get(i), i);
		}
		
		for (int i = 0; i < N; i++) {
			int cnt = map.get(numbers[i]);
			bw.write(cnt + " ");
		}
		bw.flush();
		bw.close();
	}
}
