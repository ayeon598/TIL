package ex_2025;

import java.util.*;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int result = 0;
		for (int i = 1; i <= N; i++) {
			result += i;
		}
		System.out.print(result);
	}
}
