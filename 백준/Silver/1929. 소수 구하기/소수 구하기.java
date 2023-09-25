import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb;
    static StringTokenizer st;
    static boolean[] prime;
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        sb = new StringBuilder();

        prime = new boolean[N + 1];
        Arrays.fill(prime, true);

        for (int i = 2; i < N + 1; i++) {
            if (prime[i]) {
                if (i >= M) {
                    sb.append(i).append('\n');
                }
                for (int j = 2 * i; j < N + 1; j += i) {
                    prime[j] = false;
                }
            }
        }
        System.out.println(sb.toString());
    }
}
