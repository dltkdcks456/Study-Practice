import java.io.*;
import java.util.*;
public class Main {
    static int N, M;
    static int[] countArr;
    static ArrayList<ArrayList<Node>> graph;
    static class Node{
        int idx;
        public Node(int idx) {
            this.idx = idx;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        graph = new ArrayList<>();
        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<>());
        }
        countArr = new int[N + 1];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(new Node(b));
            countArr[b]++;
        }

        Queue<Node> q = new LinkedList<>();
        for (int i = 1; i < N + 1; i++) {
            if (countArr[i] == 0) {
                q.offer(new Node(i));
            }
        }
        StringBuilder sb = new StringBuilder();
        while(!q.isEmpty()) {
            Node v = q.poll();
            sb.append(v.idx + " ");
            for (int i = 0; i < graph.get(v.idx).size(); i++) {
                Node currNode = graph.get(v.idx).get(i);
                countArr[currNode.idx]--;
                if (countArr[currNode.idx] == 0) {
                    q.offer(currNode);
                }
            }
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}
