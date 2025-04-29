import java.util.*;

public class Bronz2480 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		if (a == b && b == c) {
			int res = 10000 + a*1000;
			System.out.println(res);
		} else if (a == b || b == c) {
			int res = 1000 + b*100;
			System.out.println(res);
		} else if (a == c) {
			int res = 1000 + a*100;
			System.out.println(res);
		} else {
			int res = Math.max(Math.max(a, b), c)*100;
			System.out.println(res);
		}
	}
}
