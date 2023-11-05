import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int N, v, w;
    static int[] weight, visited;
    static int[][] dp;
    static ArrayList<Integer>[] adjList;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        weight = new int[N + 1];
        adjList = new ArrayList[N + 1];
        for (int i = 0; i < N + 1; i++) {
            adjList[i] = new ArrayList<>();
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < N + 1; i++) {
            weight[i] = Integer.parseInt(st.nextToken());
        }
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            v = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());
            adjList[v].add(w);
            adjList[w].add(v);
        }
        dp = new int[N + 1][2];
        visited = new int[N + 1];
        DFS(1);
        System.out.println(Math.max(dp[1][0], dp[1][1]));
    }
    static void DFS(int currNode) {
        int size = adjList[currNode].size();

        dp[currNode][0] = 0;
        dp[currNode][1] = weight[currNode];

        if (size == 0) return;

        visited[currNode] = 1;
        for (int nextNode : adjList[currNode]) {
            if (visited[nextNode] == 0) {
                DFS(nextNode);
                dp[currNode][1] += dp[nextNode][0];
                dp[currNode][0] += Math.max(dp[nextNode][0], dp[nextNode][1]);
            }
        }
    }
}
