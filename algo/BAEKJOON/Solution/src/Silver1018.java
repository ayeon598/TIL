import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Silver1018 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] size = br.readLine().split(" ");
		int N = Integer.parseInt(size[0]);
		int M = Integer.parseInt(size[1]);
		String[] input = new String[N];
		int[][] arr = new int[N][M];
		int minCnt = Integer.MAX_VALUE;
		
		for (int i = 0; i < N; i++) {
			input[i] = br.readLine();
			for (int j = 0; j < M; j++) {
				Character ch = input[i].charAt(j);
				if (ch == 'W') {
					arr[i][j] = 0;
				} else {
					arr[i][j] = 1;
				}
			}
		}
		for (int i = 0; i <= N-8; i++) {
			for (int j = 0; j <= M-8; j++) {
				int cnt = 0;
				int cntRe = 0;
				int start = arr[i][j];
				for (int k = 0; k < 8; k++){
					for (int l = 0; l < 8; l++) {
						if ((k + l) % 2 == 0) {
							if (arr[i+k][j+l] != start) {
								cnt += 1;
							} else {
								cntRe += 1;
							}
						} else {
							if (arr[i+k][j+l] == start) {
								cnt += 1;
							} else {
								cntRe += 1;
							}
						}
					}
				}
				cnt = Math.min(cnt, cntRe);
				minCnt = Math.min(minCnt, cnt);
			}
		}
		System.out.println(minCnt);
	}
}
