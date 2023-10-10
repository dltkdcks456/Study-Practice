import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static long[] arr, restArr;
    static long[] sumV;
    static int N, M;
    static long cnt;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new long[N + 1];
        sumV = new long[N + 1];
        restArr = new long[M];
        st = new StringTokenizer(br.readLine());

        for (int i = 1; i < N + 1; i++) {
            arr[i] = Integer.parseInt(st.nextToken()) % M;
        }

        for (int i = 1; i < N + 1; i++) {
            sumV[i] = (sumV[i - 1] + arr[i]) % M;
            restArr[(int) sumV[i]]++;
        }

        cnt = restArr[0];

        for (int i = 0; i < M; i++) {
            if (restArr[i] >= 2) {
                cnt += (restArr[i] * (restArr[i] - 1)) / 2;
            }
        }
        System.out.println(cnt);
    }


}
