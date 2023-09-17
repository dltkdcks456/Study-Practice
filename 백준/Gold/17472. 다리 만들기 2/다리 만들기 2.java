import java.io.*;
import java.util.*;

public class Main {
    static int[] dr, dc, parents;
    static int N, M;
    static int[][] visited, land;
    static PriorityQueue<Node> q;

    static class Node implements Comparable<Node>{
        int start;
        int des;
        int cost;
        public Node(int start, int des, int cost) {
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

    static class Pos{
        int r;
        int c;
        public Pos(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    public static void checkNode(int r, int c, int node) {
        for (int d = 0; d < 4; d++) {
            int multi = 1;
            int cnt = 0;
            while(true) {
                int newR = r + dr[d] * multi;
                int newC = c + dc[d] * multi;

                if (newR < N && newR >= 0 && newC < M && newC >= 0) {
                    if (land[newR][newC] == node) {
                        break;
                    }
                    if (land[newR][newC] != 0) {
                        if (cnt >= 2) {
                            q.offer(new Node(node, land[newR][newC], cnt));
                            break;
                        } else {
                            break;
                        }
                    } else {
                        cnt++;
                        multi++;
                    }
                } else {
                    break;
                }
            }
        }
    }

    public static void BFS(int r, int c, int k) {
        Queue<Pos> q = new LinkedList<>();
        q.offer(new Pos(r, c));
        visited[r][c] = 1;
        land[r][c] = k;
        while(!q.isEmpty()) {
            Pos v = q.poll();
            int currR = v.r;
            int currC = v.c;
            for (int d = 0; d < 4; d++) {
                int newR = currR + dr[d];
                int newC = currC + dc[d];
                if (newR < N && newR >= 0 && newC < M && newC >= 0 && land[newR][newC] == 1 && visited[newR][newC] == 0) {
                    visited[newR][newC] = 1;
                    land[newR][newC] = k;
                    q.offer(new Pos(newR, newC));
                }
            }
        }
    }

    public static void union(int a, int b) {
        int A = find(a);
        int B = find(b);
        parents[B] = A;
    }
    public static int find(int x) {
        if (parents[x] == x) {
            return x;
        }
        return parents[x] = find(parents[x]);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        dr = new int[]{0, 1, 0, -1};
        dc = new int[]{1, 0, -1, 0};
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        land = new int[N][M];
        visited = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                land[i][j] = Integer.parseInt(st.nextToken());
            }
        }


        int landNo = 1;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (land[i][j] == 1 && visited[i][j] == 0) {
                    BFS(i, j, landNo);
                    landNo++;
                }
            }
        }

        q = new PriorityQueue<>();
        parents = new int[landNo];
        for (int i = 0; i < landNo; i++) {
            parents[i] = i;
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (land[i][j] > 0) {
                    checkNode(i, j, land[i][j]);
                }
            }
        }

        int sumV = 0;

        while(!q.isEmpty()) {
            Node currNode = q.poll();
            if (find(currNode.start) != find(currNode.des)) {
                union(currNode.start, currNode.des);
                sumV += currNode.cost;
            }
        }
        int par = find(parents[1]);
        boolean flag = true;
        for (int i = 2; i < parents.length; i++) {
            if (find(i) != par) {
                flag = false;
            }
        }
        System.out.println(flag ? sumV : -1);
    }
}
