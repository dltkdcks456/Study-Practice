import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static long[][] points;

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        points = new long[N][2];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            points[i] = new long[] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
        }
        double sumV = 0;
        for (int i = 0; i < N; i++) {
            sumV += getArea(points[i], points[(i + 1) % N]);
        }
        System.out.printf("%.1f", Math.abs(sumV));
    }
    static double getArea(long[] A, long[] B) {
        return (double) (A[0] * B[1] - A[1] * B[0]) / 2;
    }
}
