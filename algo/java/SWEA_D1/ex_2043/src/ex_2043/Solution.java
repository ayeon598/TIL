package ex_2043;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int P = sc.nextInt();
		int K = sc.nextInt();
		int cnt = 1;
		while(P != K) {
			cnt += 1;
			K += 1;
		}
		System.out.println(cnt);
	}
}
