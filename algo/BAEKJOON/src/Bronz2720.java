import java.io.*;

public class Bronz2720 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++){
            int C = Integer.parseInt(br.readLine());
            int Q = C / 25;
            C %= 25;
            int D = C / 10;
            C %= 10;
            int N = C / 5;
            int P = C % 5;
            bw.write(Q + " " + D + " " + N + " " + P);
            bw.newLine();
        }
        bw.flush();
        bw.close();
    }
}
