package ex_2068;

import java.util.*;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int i=1; i<= T; i++) {
			int maxNum = 0;
			for (int j=1; j<=10; j++) {
				int number = sc.nextInt();
				if (maxNum < number) {
				maxNum = number;
				}
			}
			System.out.println("#" + i + " " + maxNum);
		}
	}
}
