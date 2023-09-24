import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static Product[] pr;
    static int[][] dp;
    static class Product{
        int weight;
        int value;
        public Product(int weight, int value) {
            this.weight = weight;
            this.value = value;
        }
    }
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        dp = new int[N + 1][K + 1];
        pr = new Product[N + 1];
        for (int i = 1; i < N + 1; i++) {
            st = new StringTokenizer(br.readLine());
            int W = Integer.parseInt(st.nextToken());
            int V = Integer.parseInt(st.nextToken());
            pr[i] = new Product(W, V);
        }

        for (int i = 1; i < K + 1; i++) {
            for (int j = 1; j < N + 1; j++) {
                if (pr[j].weight > i) {
                    dp[j][i] = dp[j - 1][i];
                } else {
                    dp[j][i] = Math.max(dp[j - 1][i - pr[j].weight] + pr[j].value, dp[j - 1][i]);
                }
            }
        }

        System.out.println(dp[N][K]);


    }

}
