package ex_2019;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int result;
		for (int i=0; i <=N; i++) {
			result = (int)Math.pow(2, i);
			System.out.print(result + " ");
		}
	}
}
