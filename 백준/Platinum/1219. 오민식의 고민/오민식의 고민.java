import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static long INF = -Integer.MAX_VALUE;
    static long[] dist;
    static int[] income, visited;
    static ArrayList<Edge>[] graph;
    static int N, start, M, end;

    static class Edge{
        int idx;
        int cost;
        public Edge(int idx, int cost) {
            this.idx = idx;
            this.cost = cost;
        }
    }

    static boolean BFS(int i) {
        Queue<Integer> q = new LinkedList<>();
        q.add(i);
        visited[i] = 1;
        while(!q.isEmpty()) {
            int v = q.poll();
            if (v == end) {
                return true;
            }
            for (Edge e : graph[v]) {
                if (visited[e.idx] == 0) {
                    visited[e.idx] = 1;
                    q.add(e.idx);
                }
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        start = Integer.parseInt(st.nextToken());
        end = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph[s].add(new Edge(e, c));
        }

        income = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            income[i] = Integer.parseInt(st.nextToken());
        }

        dist = new long[N];
        Arrays.fill(dist, INF);
        dist[start] = income[start];
        boolean flag = false;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (Edge edge : graph[j]) {
                    if ((dist[j] != INF) && (dist[edge.idx] < dist[j] + income[edge.idx] - edge.cost)) {
                        dist[edge.idx] = dist[j] + income[edge.idx] - edge.cost;
                        if (i == N - 1) {
                            visited = new int[N];
                            boolean check = BFS(j);
                            if (check) {
                                flag = true;
                                break;
                            }
                        }
                    }
                }
            }
            if (flag) {
                break;
            }
        }

        if (flag) {
            System.out.println("Gee");
        } else {
            if (dist[end] == INF) {
                System.out.println("gg");
            } else {
                System.out.println(dist[end]);
            }
        }

    }
}
