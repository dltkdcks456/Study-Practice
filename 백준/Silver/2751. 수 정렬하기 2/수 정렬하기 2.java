import java.io.*;

public class Main {
    static int[] arr;
    static int[] tmp;
    static void merge(int s, int e) {
        if (s < e) {
            int m = (s + e) / 2;
            merge(s, m);
            merge(m + 1, e);

            int l = s, r = m + 1;
            int idx = l;

            while(l <= m || r <= e) {
                if (r > e || (l <= m && arr[l] < arr[r])) {
                    tmp[idx++] = arr[l++];
                } else {
                    tmp[idx++] = arr[r++];
                }
            }
            for (int i = s; i <= e; i++) {
                arr[i] = tmp[i];
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        arr = new int[N];
        tmp = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        merge(0, N - 1);
        for(int i : arr) {
            bw.write(i + "\n");
        }
        bw.flush();
        bw.close();
    }
}
