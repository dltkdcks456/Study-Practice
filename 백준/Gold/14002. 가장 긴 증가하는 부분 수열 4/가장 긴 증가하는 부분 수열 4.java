import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int N, lastIdx;
    static int[] arr, dp, ans;
    static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        arr = new int[N];
        dp = new int[N + 1];
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        dp[1] = arr[0];
        lastIdx = 1;
        ans = new int[N];
        ans[0] = 1;

        for (int i = 1; i < N; i++) {
            if (dp[lastIdx] < arr[i]) {
                dp[++lastIdx] = arr[i];
                ans[i] = lastIdx;
                continue;
            }
            int s = 1;
            int e = lastIdx;
            boolean flag = false;
            while (s <= e) {
                int m = (s + e) / 2;
                if (dp[m] == arr[i]) {
                    flag = true;
                    ans[i] = m;
                    break;
                } else if(dp[m] > arr[i]) {
                    e = m - 1;
                } else {
                    s = m + 1;
                }
            }
            if (!flag) {
                dp[s] = arr[i];
                ans[i] = s;
            }

        }


        Deque<Integer> q = new LinkedList<>();
        sb = new StringBuilder();

        sb.append(lastIdx).append("\n");

        for (int i = N - 1; i > -1 ; i--) {
            if (ans[i] == lastIdx) {
                lastIdx--;
                q.addFirst(arr[i]);
                if (lastIdx < 0) {
                    break;
                }
            }
        }

        while(!q.isEmpty()) {
            int tmp = q.poll();
            sb.append(tmp).append(" ");
        }
        System.out.println(sb);
    }
}
