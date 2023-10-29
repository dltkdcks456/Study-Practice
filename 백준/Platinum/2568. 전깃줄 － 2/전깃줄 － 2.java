import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int N, lastIdx;
    static int[][] arr;
    static int[] dp, idxArr;
    static boolean[] checkArr;
    static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        arr = new int[N][2];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i] = new int[] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
        }

        Comparator<int[]> cmp = new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        };

        Arrays.sort(arr, cmp);

        dp = new int[N + 1];
        idxArr = new int[N];

        dp[1] = arr[0][1];
        idxArr[0] = 1;
        lastIdx = 1;

        for (int i = 1; i < N; i++) {
            int s = 1;
            int e = lastIdx;
            boolean flag = false;
            while(s <= e) {
                int m = (s + e) / 2;
                if(dp[lastIdx] < arr[i][1]) {
                    dp[++lastIdx] = arr[i][1];
                    idxArr[i] = lastIdx;
                    flag = true;
                    break;
                } else {
                    if (dp[m] == arr[i][1]) {
                        idxArr[i] = m;
                        break;
                    } else if (dp[m] > arr[i][1]) {
                        e = m - 1;
                    } else {
                        s = m + 1;
                    }
                }

            }
            if (!flag) {
                dp[s] = arr[i][1];
                idxArr[i] = s;
            }
        }

        checkArr = new boolean[N];
        sb = new StringBuilder();
        int cnt = N - lastIdx;
        sb.append(N - lastIdx).append('\n');

        for (int i = N - 1; i > -1 ; i--) {
            if (idxArr[i] == lastIdx) {
                checkArr[i] = true;
                lastIdx--;
                if (lastIdx == 0) {
                    break;
                }
            }
        }
        if (cnt != 0) {
            for (int i = 0; i < N; i++) {
                if (!checkArr[i]) {
                    sb.append(arr[i][0]).append('\n');
                }
            }
        }

        System.out.println(sb);
    }
}
