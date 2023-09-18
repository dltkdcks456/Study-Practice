import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static ArrayList<ArrayList<Node>> graph;
    static int[] countArr;
    static long[] time, answer;
    static class Node{
        int idx;

        public Node(int idx) {
            this.idx = idx;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        countArr = new int[N + 1];
        time = new long[N + 1];
        answer = new long[N + 1];
        graph = new ArrayList<>();
        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 1; i < N + 1; i++) {
            st = new StringTokenizer(br.readLine());
            int num = st.countTokens();
            long t = Integer.parseInt(st.nextToken());
            time[i] = t;
            for (int j = 0; j < num - 2; j++) {
                int idx = Integer.parseInt(st.nextToken());
                graph.get(idx).add(new Node(i));
                countArr[i]++;
            }
        }

        Queue<Node> q = new ArrayDeque<>();
        for (int i = 1; i < N + 1; i++) {
            if (countArr[i] == 0) {
                q.offer(new Node(i));
            }
        }

        while(!q.isEmpty()) {
            Node v = q.poll();
            answer[v.idx] += time[v.idx];
            for (int i = 0; i < graph.get(v.idx).size(); i++) {
                Node currNode = graph.get(v.idx).get(i);
                countArr[currNode.idx]--;
                if (answer[currNode.idx] < answer[v.idx]) {
                    answer[currNode.idx] = answer[v.idx];
                }
                if (countArr[currNode.idx] == 0) {
                    q.offer(new Node(currNode.idx));
                }
            }
        }

        for (int i = 1; i < N + 1; i++) {
            System.out.println(answer[i]);
        }
    }
}
