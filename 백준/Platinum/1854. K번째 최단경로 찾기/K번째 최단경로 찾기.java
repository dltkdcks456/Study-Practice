import java.io.*;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static ArrayList<ArrayList<Node>> graph;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static PriorityQueue<Integer>[] dist;
    static int N, M, K;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        graph = new ArrayList<>();
        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph.get(a).add(new Node(b, c));
        }
        dist = new PriorityQueue[N + 1];
        for (int i = 0; i < N + 1; i++) {
            PriorityQueue<Integer> p = new PriorityQueue<>(K, cmp);
            dist[i] = p;
        }

        PriorityQueue<Node> q = new PriorityQueue<>();
        q.offer(new Node(1, 0));
        dist[1].offer(0);
        while(!q.isEmpty()) {
            Node currNode = q.poll();
            for (int i = 0; i < graph.get(currNode.idx).size(); i++) {
                Node nxtNode = graph.get(currNode.idx).get(i);
                // 거리값 K개 채워주기
                if (dist[nxtNode.idx].size() < K) {
                    dist[nxtNode.idx].offer(currNode.dist + nxtNode.dist);
                    q.add(new Node(nxtNode.idx, currNode.dist + nxtNode.dist));
                } else {
                    // 거리를 비교해서 Max값보다 작은 경우 넣어주기
                    if (dist[nxtNode.idx].peek() > currNode.dist + nxtNode.dist) {
                        dist[nxtNode.idx].poll();
                        dist[nxtNode.idx].offer(currNode.dist + nxtNode.dist);
                        q.add(new Node(nxtNode.idx, currNode.dist + nxtNode.dist));
                    }
                }
            }
        }
        int answer = 0;
        for (int i = 1; i < dist.length; i++) {
            if (dist[i].size() < K) {
                bw.write("-1\n");
            } else {
                bw.write(String.valueOf(dist[i].peek()) + "\n");
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }
    static Comparator<Integer> cmp = new Comparator<Integer>() {
        @Override
        public int compare(Integer o1, Integer o2) {
            if (o1 > o2) return -1;
            else if (o1 < o2) return 1;
            else return 0;
        }
    };
    static class Node implements Comparable<Node>{
        int idx;
        int dist;
        public Node(int idx, int dist) {
            this.idx = idx;
            this.dist = dist;
        }

        @Override
        public int compareTo(Node o) {
            if (this.dist > o.dist) return 1;
            else if (this.dist < o.dist) return -1;
            else return 0;
        }
    }
}
