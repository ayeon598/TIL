package ex_2046;

import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		String ans = "";
		for(int i=0; i<N; i++){
			ans += '#';
		}
		System.out.println(ans);
	}
}
