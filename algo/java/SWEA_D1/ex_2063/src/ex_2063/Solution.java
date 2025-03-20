package ex_2063;

import java.util.*;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int mid = N / 2;
		ArrayList<Integer> numbers = new ArrayList<>();
		for(int i=1; i<=N; i++) {
			numbers.add(sc.nextInt());
		}
		Collections.sort(numbers);
		System.out.println(numbers.get(mid));
	}
}
