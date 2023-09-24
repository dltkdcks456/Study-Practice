import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static Edge[] graph;
    static long[] dist;
    static int INF = Integer.MAX_VALUE;
    static class Edge{
        int startIdx;
        int endIdx;
        int cost;
        public Edge(int startIdx, int endIdx, int cost) {
            this.startIdx = startIdx;
            this.endIdx = endIdx;
            this.cost = cost;
        }
    }
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        graph = new Edge[M];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph[i] = new Edge(a, b, c);
        }

        dist = new long[N + 1];
        Arrays.fill(dist, INF);
        dist[1] = 0;

        boolean flag = false;

        for (int i = 0; i < N; i++) {
            for (Edge edge : graph) {
                if ((dist[edge.startIdx] != INF) && (dist[edge.endIdx] > dist[edge.startIdx] + edge.cost)) {
                    dist[edge.endIdx] = dist[edge.startIdx] + edge.cost;
                    if (i == N - 1) {
                        flag = true;
                        break;
                    }
                }
            }
        }

        if (flag) {
            System.out.println(-1);
        } else {
            for (int i = 2; i < N + 1; i++) {
                if (dist[i] != INF) {
                    System.out.println(dist[i]);
                } else {
                    System.out.println(-1);
                }
            }
        }
    }
}
