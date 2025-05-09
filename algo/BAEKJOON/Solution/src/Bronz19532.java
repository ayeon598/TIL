import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Bronz19532 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String[] input = br.readLine().split(" ");
		int a = Integer.parseInt(input[0]);
		int b = Integer.parseInt(input[1]);
		int c = Integer.parseInt(input[2]);
		int d = Integer.parseInt(input[3]);
		int e = Integer.parseInt(input[4]);
		int f = Integer.parseInt(input[5]);
		int x, y;
		x = (c*e - f*b) / (a*e - d*b);
		y = (c*d - f*a) / (b*d - e*a);
		bw.write(x + " " + y);
		bw.flush();
		bw.close();
		
	}
}
