package ex_2027;

public class Solution {
	public static void main(String[] args) {
		int index = 0;
		String a = "#";
		String b = "+";
		for (int i=1; i<=5; i++) {
			for (int j=0; j<5; j++) {
				if (index == j) {
					System.out.print(a+"");
				} else {
					System.out.print(b+"");
				}
			}
			index += 1;
			System.out.println();
		}
	}
}
