import java.io.*;

public class Bronz3009 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] sumX = new int[2];
        int[] sumY = new int[2];

        for (int i = 0; i < 3; i++) {
            String[] input = br.readLine().split(" ");
            int x = Integer.parseInt(input[0]);
            int y = Integer.parseInt(input[1]);
            if (x == sumX[0]) {
                sumX[0] = 0;
            } else if (x == sumX[1]) {
                sumX[1] = 0;
            } else if (sumX[0] == 0) {
                sumX[0] = x;
            } else {
                sumX[1] = x;
            }
            if (y == sumY[0]) {
                sumY[0] = 0;
            } else if (y == sumY[1]) {
                sumY[1] = 0;
            } else if (sumY[0] == 0) {
                sumY[0] = y;
            } else {
                sumY[1] = y;
            }
        }
        int resX = 0;
        int resY = 0;
        if (sumX[0] != 0) {
            resX = sumX[0];
        } else {
            resX = sumX[1];
        }
        if (sumY[0] != 0) {
            resY = sumY[0];
        } else {
            resY = sumY[1];
        }
        bw.write(resX + " " + resY);
        bw.flush();
        bw.close();
    }
}
