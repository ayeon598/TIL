package ex_2029;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int t=1; t<=T; t++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int result = a / b;
			
			System.out.println("#" + t + " " + result + " " + a%b);
		}
	}
}
