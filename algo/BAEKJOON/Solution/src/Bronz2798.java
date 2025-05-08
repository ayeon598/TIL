import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Bronz2798 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] input = br.readLine().split(" ");
		int N = Integer.parseInt(input[0]);
		int M = Integer.parseInt(input[1]);
		String[] cards = br.readLine().split(" ");
		int[] card = new int[N];
		int res = 0;
		
		for (int i = 0; i < N; i++) {
			card[i] = Integer.parseInt(cards[i]);
		}
		Arrays.sort(card);
		
		for (int i = 0; i < N-2; i++) {
			int card1 = card[i];
			if (card1 >= M) {
				break;
			}
			for (int j = i+1; j < N-1; j++) {
				int card2 = card[j];
				if (card1+card2 >= M) {
					break;
				}
				for (int k = j+1; k < N; k++) {
					int card3 = card[k];
					if (card1+card2+card3 > M) {
						break;
					} else if (card1+card2+card3 == M) {
						res = M;
						break;
					} else {
						res = Math.max(res, card1+card2+card3);
					}
				}
			}
		}
		System.out.println(res);
	}
}
