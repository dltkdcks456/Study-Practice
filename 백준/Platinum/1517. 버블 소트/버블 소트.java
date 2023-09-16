import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static int[] arr, tmp;
    public static long cnt;
    public static void merge(int s, int e) {
        if (s < e) {
            int m = (s + e) / 2;

            merge(s, m);
            merge(m + 1, e);

            int l = s, r = m + 1;
            int idx = l;

            while(l <= m && r <= e) {
                if (arr[l] > arr[r]) {
                    tmp[idx++] = arr[r++];
                    cnt += r - idx;
                } else {
                    tmp[idx++] = arr[l++];
                }
            }
            while(l <= m) {
                tmp[idx++] = arr[l++];

            }
            while(r <= e) {
                tmp[idx++] = arr[r++];
            }
            for (int i = s; i <= e; i++) {
                arr[i] = tmp[i];
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        arr = new int[N];
        tmp = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        merge(0, N - 1);
        bw.write(String.valueOf(cnt));
        bw.flush();
        bw.close();

    }
}
