import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[][] points;

    public static void main(String[] args) throws IOException {
        points = new int[3][2];
        for (int i = 0; i < 3; i++) {
            st = new StringTokenizer(br.readLine());
            points[i] = new int[] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
        }

        System.out.println(ccw(points[0], points[1], points[2]));

    }
    static int ccw(int[] P1, int[] P2, int[] P3) {
        int[] P12 = new int[] {P2[0] - P1[0], P2[1] - P1[1]};
        int[] P13 = new int[] {P3[0] - P1[0], P3[1] - P1[1]};
        int result = P12[0] * P13[1] - P12[1] * P13[0];
        if (result > 0) return 1;
        else if (result == 0) return 0;
        else return -1;
    }
}
