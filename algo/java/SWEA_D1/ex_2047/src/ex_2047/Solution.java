package ex_2047;

import java.util.*;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
		String answer = "";
		char a;
		for(int i=0; i<str.length(); i++) {
			a = str.charAt(i);
			if(Character.isLowerCase(a)) {
				answer += Character.toUpperCase(a);
			} else {
				answer += a;
			}
		}
		System.out.println(answer);
	}
}
