import java.io.*;

public class Bronz15552 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		long t = Long.parseLong(br.readLine());
		for (int i = 0; i < t; i++) {
			String[] input = br.readLine().split(" ");
			int a = Integer.parseInt(input[0]);
			int b = Integer.parseInt(input[1]);
			int res = a + b;
//			bw.write(Integer.toString(res));
			bw.write(res+"");
			if (i < (t-1)) {
				bw.newLine();
			}
		}
		bw.flush();
		bw.close();
	}
}
