import java.io.*;

public class Bronz9506 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = 0;
        while (n != -1) {
            n = Integer.parseInt(br.readLine());
            int sumN = 0;
            String num = "";
            if (n == -1) {
                break;
            }
            for (int i = 1; i < n; i++) {
                if (n % i == 0) {
                    sumN += i;
                    num += (i + " ");
                }
            }
            String[] res = num.split(" ");
            if (sumN == n) {
                bw.write(n + " = ");
                for (int i = 0; i < res.length; i++) {
                    bw.write(res[i]);
                    if (i < res.length-1) {
                        bw.write(" + ");
                    }
                }
            } else {
                bw.write(n + " is NOT perfect.");
            }
            bw.newLine();
        }
        bw.flush();
        bw.close();
    }
}
