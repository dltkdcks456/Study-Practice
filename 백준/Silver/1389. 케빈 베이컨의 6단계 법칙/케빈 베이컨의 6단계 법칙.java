import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static long[][] dp;
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        dp = new long[N + 1][N + 1];

        for (int i = 1; i < N + 1; i++) {
            for (int j = 1; j < N + 1; j++) {
                if (i == j) {
                    dp[i][j] = 0;
                } else {
                    dp[i][j] = Integer.MAX_VALUE;
                }
            }
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            dp[a][b] = 1;
            dp[b][a] = 1;
        }

        for (int k = 1; k < N + 1; k++) {
            for (int i = 1; i < N + 1; i++) {
                for (int j = 1; j < N + 1; j++) {
                    dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k][j]);
                }
            }
        }

        int minV = Integer.MAX_VALUE;
        int answer = Integer.MAX_VALUE;
        for (int i = 1; i < N + 1; i++) {
            int sumV = 0;
            for (int j = 1; j < N + 1; j++) {
                if ((i != j) && (dp[j][i] != Integer.MAX_VALUE)) {
                    sumV += dp[j][i];
                }
            }
            if (minV > sumV) {
                minV = sumV;
                answer = i;
            }
        }
        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
    }
}
