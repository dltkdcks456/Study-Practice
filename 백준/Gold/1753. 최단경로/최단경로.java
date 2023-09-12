import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static class Node {
        // 변수
        int idx;
        int cost;
        // 생성자
        public Node(int idx, int cost) {
            this.idx = idx;
            this.cost = cost;
        }
    }
    public static void main(String[] args) throws IOException {
        // buffer를 활용해서 입출력 -> 빠른 속도
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        // 공백 단위로 끊어줌 -> split처럼 쪼개서 사용 가능
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        int start = Integer.parseInt(br.readLine());

        // 노드의 정보를 담을 리스트 생성
        ArrayList<ArrayList<Node>> graph = new ArrayList<ArrayList<Node>>();
        // 노드가 들어갈 내부 리스트 생성
        for(int i = 0; i < V + 1; i++) {
            graph.add(new ArrayList<Node>());
        }
        // 노드 정보 입력
        for(int j = 0; j < E; j++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph.get(u).add(new Node(v, w));
        }

        // 거리 정보
        int[] dist = new int[V + 1];
        // 최댓값으로 초기화

        Arrays.fill(dist, Integer.MAX_VALUE);
        // 출발값은 거리 0
        dist[start] = 0;

        // 우선순위 큐 활용
        PriorityQueue<Node> q = new PriorityQueue<Node>((o1, o2) -> Integer.compare(o1.cost, o2.cost));
        q.offer(new Node(start, 0));
        while(!q.isEmpty()) {
            Node currNode = q.poll();

            if(dist[currNode.idx] < currNode.cost) {
                continue;
            }

            for(int l = 0; l < graph.get(currNode.idx).size(); l++) {
                Node nxtNode = graph.get(currNode.idx).get(l);
                if (dist[nxtNode.idx] > dist[currNode.idx] + nxtNode.cost) {
                    dist[nxtNode.idx] = dist[currNode.idx] + nxtNode.cost;
                    q.offer(new Node(nxtNode.idx, dist[nxtNode.idx]));
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for(int m = 1; m < V + 1; m++) {
            sb.append(dist[m] == Integer.MAX_VALUE ? "INF\n" : dist[m] + "\n");
        }
        System.out.println(sb.toString());
    }
}
