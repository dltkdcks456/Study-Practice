import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringBuilder sb;
    static StringTokenizer st;
    static ArrayList<Integer>[] graph;
    static int[][] parents;
    static int[] tmpParents;
    static int[] depth, visited;
    static int N, Kmax, depMax;

    static void DFS(int x, int deep) {
        depth[x] = deep;
        visited[x] = 1;
        if (depMax < deep) {
            depMax = deep;
        }
        for (int n : graph[x]) {
            if (visited[n] == 0) {
                tmpParents[n] = x;
                DFS(n, deep + 1);
            }
        }
    }

    static int lca(int v, int w) {
        // w가 더 깊도록 스왑
        if (depth[v] > depth[w]) {
            int tmp = v;
            v = w;
            w = tmp;
        }
        // 깊이 동일하게 변경
        for (int i = Kmax; i > -1; i--) {
            if (depth[w] - depth[v] >= (1 << i)) {
                w = parents[i][w];
            }
        }

        // 같은 부모 찾기
        for (int i = Kmax; i > -1; i--) {
            if (parents[i][v] != parents[i][w]) {
                v = parents[i][v];
                w = parents[i][w];
            }
        }
        int lca = v;
        if (v != w) {
            lca = parents[0][lca];
        }
        return lca;
    }

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        graph = new ArrayList[N + 1];
        depth = new int[N + 1];
        visited = new int[N + 1];
        for (int i = 0; i < N + 1; i++) {
            graph[i] = new ArrayList<>();
        }
        tmpParents = new int[N + 1];
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }
        depMax = 0;
        DFS(1, 0);
        depMax++;
        int tmp = 1;
        Kmax = -1;
        while(tmp <= depMax) {
            tmp <<= 1;
            Kmax++;
        }

        parents = new int[Kmax + 1][N + 1];
        for (int i = 0; i < N + 1; i++) {
            parents[0][i] = tmpParents[i];
        }

        for (int K = 1; K < Kmax + 1; K++) {
            for (int n = 1; n < N + 1; n++) {
                parents[K][n] = parents[K - 1][parents[K - 1][n]];
            }
        }

        int M = Integer.parseInt(br.readLine());
        sb = new StringBuilder();
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
