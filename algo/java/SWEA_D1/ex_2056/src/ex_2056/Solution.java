package ex_2056;

import java.util.*;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int i=1; i<=T; i++) {
			String N = sc.next();
			String year = N.substring(0,4);
			String month = N.substring(4,6);
			String day = N.substring(6,8);
			boolean ok = false;
			if (Integer.parseInt(month) == 2) {
				if (Integer.parseInt(day) <= 28 & Integer.parseInt(day) > 0) {
					ok = true;
				}
			} else if (Integer.parseInt(month) == 1 | Integer.parseInt(month) == 3 | Integer.parseInt(month) == 5 | Integer.parseInt(month) == 7 | Integer.parseInt(month) == 8 | Integer.parseInt(month) == 10 | Integer.parseInt(month) == 12) {
				if (Integer.parseInt(day) <= 31 & Integer.parseInt(day) > 0) {
					ok = true;
				}				
			} else if (Integer.parseInt(month) == 4 | Integer.parseInt(month) == 6 | Integer.parseInt(month) == 9 | Integer.parseInt(month) == 11) {
				if (Integer.parseInt(day) <= 30 & Integer.parseInt(day) > 0) {
					ok = true;
				}
			}
			if (ok) {
				System.out.println("#" + i + " " + year + "/" + month + "/" + day);
			} else {
				System.out.println("#" + i + " " + -1);
			}
		}
	}
}
