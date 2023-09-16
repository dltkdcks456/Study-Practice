import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int[] parents;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        parents = new int[n + 1];
        for (int i = 1; i < n + 1; i++) {
            parents[i] = i;
        }
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int data = Integer.parseInt(st.nextToken());
                if (data == 1) {
                    union(i + 1, j + 1);
                }
            }
        }
        boolean answer = true;
        st = new StringTokenizer(br.readLine());
        int plan = find(Integer.parseInt(st.nextToken()));
        for (int i = 1; i < m; i++) {
            if (find(Integer.parseInt(st.nextToken())) != plan) {
                answer = false;
                break;
            }
        }
        if (answer) {
            bw.write("YES");
        } else {
            bw.write("NO");
        }
        bw.flush();
        bw.close();
    }
    public static void union(int a, int b) {
        int A = find(a);
        int B = find(b);
        parents[B] = A;
    }
    public static int find(int a) {
        if (parents[a] == a) {
            return a;
        }
        return parents[a] = find(parents[a]);
    }
}
