import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb;
    static int[][] parents;
    static int[] initPar, depth, dist;
    static ArrayList<int[]>[] adjList;
    static int N, M, maxDepth, K;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        adjList = new ArrayList[N + 1];
        for (int i = 0; i < N + 1; i++) {
            adjList[i] = new ArrayList<>();
        }
        initPar = new int[N + 1];
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            adjList[v].add(new int[] {w, c});
            adjList[w].add(new int[] {v, c});
        }

        depth = new int[N + 1];
        dist = new int[N + 1];
        maxDepth = 0;
        
        dfs(1, 0, 0);

        K = 0;
        int tmp = 1;
        while(tmp < maxDepth) {
            tmp <<= 1;
            K++;
        }

        parents = new int[K + 1][N + 1];

        for (int i = 0; i < N + 1; i++) {
            parents[0][i] = initPar[i];
        }

        for (int k = 1; k <= K; k++) {
            for (int i = 1; i <= N; i++) {
                parents[k][i] = parents[k - 1][parents[k - 1][i]];
            }
        }

        M = Integer.parseInt(br.readLine());
        sb = new StringBuilder();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int commonPar = lca(s, e);
            sb.append(dist[e] + dist[s] - 2 * dist[commonPar]).append('\n');
        }
        System.out.println(sb);
    }

    static void dfs(int currNode, int prevNode, int deepSize) {
        depth[currNode] = deepSize;
        initPar[currNode] = prevNode;
        maxDepth = Math.max(maxDepth, deepSize);
        for (int[] nextNode : adjList[currNode]) {
            if (nextNode[0] != prevNode) {
                dist[nextNode[0]] = dist[currNode] + nextNode[1];
                dfs(nextNode[0], currNode, deepSize + 1);
            }
        }
    }

    static int lca(int a, int b) {
        if (depth[a] > depth[b]) {
            int t = a;
            a = b;
            b = t;
        }

        for (int k = K; k > -1; k--) {
            if (Math.pow(2, k) <= depth[b] - depth[a]) {
                b = parents[k][b];
            }
        }

        if (a == b) return a;

        for (int k = K; k > -1; k--) {
            if (parents[k][a] != parents[k][b]) {
                a = parents[k][a];
                b = parents[k][b];
            }
        }

        if (a != b) {
            a = parents[0][a];
        }

        return a;
    }
}
