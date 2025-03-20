package ex_2058;

import java.util.*;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int sumNum = 0;
		while (N > 0) {
			sumNum += N % 10;
			N /= 10;
		}
		System.out.println(sumNum);
	}
}
