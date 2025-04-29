import java.util.*;

public class Bronz25304 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long x = sc.nextLong();
		int n = sc.nextInt();
		long res = 0;
		for (int i = 0; i < n; i++) {
			long a = sc.nextLong();
			int b = sc.nextInt();
			res += a*b;
		}
		if (x == res) {
			System.out.println("Yes");
		} else {
			System.out.println("No");
		}
	}
}
