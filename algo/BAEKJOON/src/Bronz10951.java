import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Bronz10951 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line;
        while ((line = br.readLine()) != null) { // �Է��� ���� ������
            String[] parts = line.split(" "); // ���� �������� ������
            int a = Integer.parseInt(parts[0]);
            int b = Integer.parseInt(parts[1]);
            System.out.println(a + b);
        }
    }
}