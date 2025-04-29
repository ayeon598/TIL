import java.io.*;

public class Bronz10952 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int a = -1;
		int b = -1;
		while(a != 0 || b != 0) {
			String[] input = br.readLine().split(" ");
			a = Integer.parseInt(input[0]);
			b = Integer.parseInt(input[1]);
			if (a == 0 && b == 0) {
				break;
			}
			bw.write(a+b+"");
			bw.newLine();
		}
		bw.flush();
		bw.close();
	}
}
