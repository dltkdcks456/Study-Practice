import java.io.*;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static int[] parents;
    static int sumV;
    static class Node implements Comparable<Node>{
        int start;
        int des;
        long cost;
        public Node(int start,int des, long cost) {
            this.start = start;
            this.des = des;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            if (this.cost > o.cost) {
                return 1;
            } else if (this.cost < o.cost) {
                return -1;
            } else {
                return 0;
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        parents = new int[V + 1];
        for (int i = 1; i < V + 1; i++) {
            parents[i] = i;
        }

        PriorityQueue<Node> q = new PriorityQueue<>();
        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            long C = Long.parseLong(st.nextToken());
            q.offer(new Node(A, B, C));
        }
        sumV = 0;
        while(!q.isEmpty()) {
            Node currNode = q.poll();
            if (find(currNode.start) != find(currNode.des)) {
                union(currNode.start, currNode.des);
                sumV += currNode.cost;
            }
        }
        System.out.println(sumV);

    }
    static void union(int a, int b) {
        int A = find(a);
        int B = find(b);
        parents[B] = A;
    }
    static int find(int x) {
        if (x == parents[x]) {
            return x;
        }
        return parents[x] = find(parents[x]);
    }
}
