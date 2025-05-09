import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Bronz2231 {
	static int input;
//	static int result;
//	static boolean found = false;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		input = Integer.parseInt(br.readLine());
//		dfs("", 0);
//		System.out.println(result);
		int result = 0;
		for (int i = 0; i < input; i++) {
			int sum = i;
			int num = i;
			while (num > 0) {
				sum += num%10;
				num /= 10;
			}
			if (sum == input) {
				result = i;
				break;
			}
		}
		System.out.println(result);	
	}
//	static void dfs(String res, int depth) {
//        if (found || depth > 6) return;
//        if (!res.isEmpty()) {
//            int num = Integer.parseInt(res);
//            int sum = num;
//
//            for (char ch : res.toCharArray()) {
//                sum += ch - '0';
//            }
//
//            if (sum == input) {
//                result = num;
//                found = true;
//                return;
//            }
//        }
//
//        for (int i = 0; i <= 9; i++) {
//            if (res.isEmpty() && i == 0) continue;
//            dfs(res + i, depth + 1);
//        }
//    }
}
