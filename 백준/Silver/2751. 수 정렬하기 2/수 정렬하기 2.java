import java.io.*;

public class Main {
    static int[] arr;

    static int[] merge(int s, int e) {
        if(s == e) {
            return new int[]{arr[s]};
        }
        int m = (s + e) / 2;
        int[] A = merge(s, m);
        int[] B = merge(m + 1, e);

        int lenA = A.length;
        int lenB = B.length;

        int[] C = new int[lenA + lenB];
        int l = 0, r = 0;
        int idx = 0;

        while(l < lenA || r < lenB) {
            if (r == lenB || (l < lenA && A[l] < B[r])) {
                C[idx++] = A[l++];
            } else {
                C[idx++] = B[r++];
            }
        }
        return C;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        int answer[] = merge(0, N - 1);
        for(int i : answer) {
            bw.write(i + "\n");
        }
        bw.flush();
        bw.close();
    }
}
