import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static ArrayList<Integer>[] graph;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[] parents;
    static int N, cnt, root;
    static void DFS(int node) {
        boolean flag = true;
        for (int i = 0; i < graph[node].size(); i++) {
            flag = false;
            DFS(graph[node].get(i));
        }
        if (flag) cnt++;
    }

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        root = 0;
        cnt = 0;
        StringTokenizer st;
        parents = new int[N];
        graph = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            graph[i] = new ArrayList<>();
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());
            parents[i] = num;
            if (num != -1) {
                graph[num].add(i);
            } else {
                root = i;
            }
        }
        int EraseNode = Integer.parseInt(br.readLine());

        if (EraseNode != root) {
            graph[parents[EraseNode]].remove(Integer.valueOf(EraseNode));
            DFS(root);
        }
        
        System.out.println(cnt);
    }
}
