import java.io.*;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static int N, totalSumV;
    static char[][] computers;
    static int[] parents;
    static PriorityQueue<Node> q;

    static class Node implements Comparable<Node>{
        int start;
        int des;
        int len;
        public Node(int start, int des, int len) {
            this.start = start;
            this.des = des;
            this.len = len;
        }

        @Override
        public int compareTo(Node o) {
            if (this.len > o.len) {
                return 1;
            } else if(this.len < o.len) {
                return -1;
            } else {
                return 0;
            }
        }
    }
    static void union(int a, int b) {
        int A = find(a);
        int B = find(b);
        parents[B] = A;
    }
    static int find(int x) {
        if (parents[x] == x) {
            return x;
        }
        return parents[x] = find(parents[x]);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        computers = new char[N][N];
        parents = new int[N];
        for (int i = 1; i < N; i++) {
            parents[i] = i;
        }
        totalSumV = 0;
        for (int i = 0; i < N; i++) {
            String input = br.readLine();
            for (int j = 0; j < N; j++) {
                computers[i][j] = input.charAt(j);
                if (computers[i][j] != '0') {
                    if (Character.isUpperCase(computers[i][j])) {
                        totalSumV += (int) computers[i][j] - 38;
                    } else {
                        totalSumV += (int) computers[i][j] - 96;
                    }
                }
            }
        }

        q = new PriorityQueue<>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (computers[i][j] != '0') {
                    if (Character.isUpperCase(computers[i][j])) {
                        q.offer(new Node(i, j, (int)  (computers[i][j] - 38)));
                    } else {
                        q.offer(new Node(i, j, (int)  (computers[i][j] - 96)));
                    }

                }
            }
        }
        int sumV = 0;
        while(!q.isEmpty()) {
            Node currNode = q.poll();
            if (find(currNode.start) != find(currNode.des)) {
                union(currNode.start, currNode.des);
                sumV += currNode.len;
            }
        }

        boolean flag = true;
        int currPar = find(parents[0]);
        for (int i = 0; i < parents.length; i++) {
            if (currPar != find(parents[i])) {
                flag = false;
            }
        }
        System.out.println(flag ? totalSumV - sumV : -1);
    }
}
