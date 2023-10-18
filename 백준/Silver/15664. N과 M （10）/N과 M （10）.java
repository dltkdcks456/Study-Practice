import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb;
    static int[] arr, combArr;
    static boolean[] visited;
    static HashSet<String> set;
    static int N, M;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int inputNum = Integer.parseInt(st.nextToken());
            arr[i] = inputNum;
        }
        set = new HashSet<>();
        visited = new boolean[N];
        combArr = new int[M];
        sb = new StringBuilder();

        Arrays.sort(arr);

        comb(0, 0);
        System.out.println(sb);
    }

    static void comb(int depth, int idx) {
        if (depth == M) {
            StringBuilder sb2 = new StringBuilder();
            for (int i : combArr) {
                sb2.append(i).append(" ");
            }

            if (!set.contains(sb2.toString())) {
                sb.append(sb2).append('\n');
                set.add(sb2.toString());
            }
            return;
        }
        for (int i = idx; i < N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                combArr[depth] = arr[i];
                comb(depth + 1, i);
                visited[i] = false;
            }
        }
    }

}
