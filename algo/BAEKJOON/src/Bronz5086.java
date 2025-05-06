import java.io.*;

public class Bronz5086 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int firstNum = 1;
        int secNum = 1;
        while (firstNum != 0 || secNum != 0) {
            String[] input = br.readLine().split(" ");
            firstNum = Integer.parseInt(input[0]);
            secNum = Integer.parseInt(input[1]);
            if (firstNum == 0 && secNum == 0) {
                break;
            }

            if (secNum % firstNum == 0) {
                bw.write("factor");
                bw.newLine();
            } else if (firstNum % secNum == 0) {
                bw.write("multiple");
                bw.newLine();
            } else {
                bw.write("neither");
                bw.newLine();
            }
        }
        bw.flush();
        bw.close();
    }
}
