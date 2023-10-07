import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb;
    static int N, M;
    static int[] arr;
    static int[][] buckets;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        int unit = (int) Math.sqrt(N);

        if (N % unit != 0) {
            buckets = new int[(N / unit) + 1][2];
        } else {
            buckets = new int[(N / unit)][2];
        }

        for (int i = 0; i < buckets.length; i++) {
            buckets[i][1] = Integer.MAX_VALUE;
            int last = i * unit + unit;
            if (last >= N) {
                last = N;
            }
            for (int j = i * unit; j < last; j++) {
                if (arr[j] > buckets[i][0]) {
                    buckets[i][0] = arr[j];
                }

                if (arr[j] < buckets[i][1]) {
                    buckets[i][1] = arr[j];
                }
            }
        }

        sb = new StringBuilder();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            start -= 1;
            end -= 1;

            int maxV = 0, minV = Integer.MAX_VALUE;

            while (start % unit != 0 && start <= end) {
                if (maxV < arr[start]) {
                    maxV = arr[start];
                }
                if (minV > arr[start]) {
                    minV = arr[start];
                }
                ++start;
            }

            while ((end + 1) % unit != 0 && start <= end) {
                if (maxV < arr[end]) {
                    maxV = arr[end];
                }
                if (minV > arr[end]) {
                    minV = arr[end];
                }
                --end;
            }

            if (start < end) {
                for (int j = start / unit; j < (end / unit) + 1; j++) {
                    if (maxV < buckets[j][0]) {
                        maxV = buckets[j][0];
                    }

                    if (minV > buckets[j][1]) {
                        minV = buckets[j][1];
                    }
                }
            }

            sb.append(minV).append(" ").append(maxV).append('\n');
        }
        System.out.println(sb.toString());
    }
}
