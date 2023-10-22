import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb;
    static int[] IQs;
    static ArrayList<Integer>[] graph;

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        IQs = new int[N + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < N + 1; i++) {
            IQs[i] = Integer.parseInt(st.nextToken());
        }
        graph = new ArrayList[N + 1];
        for (int i = 0; i < N + 1; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
        }

        Comparator<int[]> cmp = new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o2[0] - o1[0];
            }
        };

        sb = new StringBuilder();

        for (int i = 1; i < N + 1; i++) {
            PriorityQueue<int[]> pq = new PriorityQueue<>(cmp);
            if (!graph[i].isEmpty()) {
                pq.add(new int[] {IQs[i], i});
                for (int next : graph[i]) {
                    pq.add(new int[] {IQs[next], next});
                }
            }

            int idx = 0;

            while(!pq.isEmpty()) {
                int[] node = pq.poll();
                if (idx == 0) {
                    idx = node[1];
                } else {
                    sb.append(idx).append(" ").append(node[1]).append('\n');
                    idx = node[1];
                }
            }
        }
        System.out.println(sb);
    }

}
