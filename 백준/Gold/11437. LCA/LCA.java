import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static StringBuilder sb;
    static int N, M;
    static ArrayList<Integer>[] graph;
    static int[] depth, parents, visited;
    public static void DFS(int x, int deep) {
        depth[x] = deep;
        visited[x] = 1;
        for (int y : graph[x]) {
            if (visited[y] == 0) {
                parents[y] = x;
                DFS(y, deep + 1);
            }
        }
    }
    public static int lca(int v, int w) {
        // 높이 맞춰주기
        while(depth[v] != depth[w]) {
            if (depth[v] > depth[w]) {
                v = parents[v];
            } else {
                w = parents[w];
            }
        }

        while(v != w) {
            v = parents[v];
            w = parents[w];
        }

        return v;
    }

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        graph = new ArrayList[N + 1];
        for (int i = 0; i < N + 1; i++) {
            graph[i] = new ArrayList<>();
        }
        parents = new int[N + 1];
        visited = new int[N + 1];
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }

        depth = new int[N + 1];
        DFS(1, 0);
        sb = new StringBuilder();
        int M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            sb.append(lca(v, w)).append("\n");
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }
}
