import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[] parents;

    public static void main(String[] args) throws IOException {
        while(true) {
            st = new StringTokenizer(br.readLine());
            int m  = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());

            if (m == 0 && n == 0) break;

            PriorityQueue<Node> pq = new PriorityQueue<>();
            parents = new int[m];
            for (int i = 0; i < m; i++) {
                parents[i] = i;
            }

            long sumV = 0;

            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                long z = Long.parseLong(st.nextToken());
                pq.add(new Node(x, y, z));
                sumV += z;
            }

            while(!pq.isEmpty()) {
                Node currNode = pq.poll();
                if (find(currNode.x) != find(currNode.y)) {
                    union(currNode.x, currNode.y);
                    sumV -= currNode.z;
                }
            }
            System.out.println(sumV);
        }

    }

    static int find(int x) {
        if (parents[x] == x) {
            return x;
        }
        return parents[x] = find(parents[x]);
    }

    static void union(int a, int b) {
        int A = find(a);
        int B = find(b);
        parents[B] = A;
    }

    static class Node implements Comparable<Node>{
        int x;
        int y;
        long z;

        public Node(int x, int y, long z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }

        @Override
        public int compareTo(Node o) {
            return (int) (this.z - o.z);
        }
    }
}
