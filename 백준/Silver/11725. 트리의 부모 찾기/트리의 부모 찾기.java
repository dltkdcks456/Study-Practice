import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static ArrayList<Integer> graph[];
    static int[] parents;
    static void find(int currNode, int prevNode) {
        parents[currNode] = prevNode;
        for (int i = 0; i < graph[currNode].size(); i++) {
            if (graph[currNode].get(i) != prevNode) {
                find(graph[currNode].get(i), currNode);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        graph = new ArrayList[N + 1];
        for (int i = 0; i < N + 1; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }
        parents = new int[N + 1];
        find(1, 0);
        for (int i = 2; i < N + 1; i++) {
            sb.append(parents[i]).append('\n');
        }
        System.out.println(sb.toString());
    }
}
