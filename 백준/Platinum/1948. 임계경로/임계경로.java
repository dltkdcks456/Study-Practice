import java.util.*;
import java.io.*;
import java.util.stream.IntStream;
 
public class Main {
 
    static int n, m, start, end;
    static int[] dist;
    static ArrayList<ArrayList<Node>> list = new ArrayList<>(),rList = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        dist = new int[n + 1];
 
        for (int i = 0; i <= n; i++) {
            list.add(new ArrayList<>());
            rList.add(new ArrayList<>());
        }
 
        for (int i = 0; i < m; i++) {
            int[] edge = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt).toArray();
            list.get(edge[0]).add(new Node(edge[1],edge[2]));
            rList.get(edge[1]).add(new Node(edge[0],edge[2]));
        }
 
        int[] input = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt).toArray();
        start = input[0]; end = input[1];
 
 
        System.out.println(findShortPath());
        System.out.println(findPathCount());
    }
 
    private static int findPathCount() {
        int ans=0;
        boolean[] visit = new boolean[n + 1];
        visit[end]=true;
        LinkedList<Integer> q = new LinkedList<>();
        q.add(end);
        while (!q.isEmpty()){
            Integer cur = q.poll();
            for (Node next : rList.get(cur)) {
                if(dist[cur]-next.cost == dist[next.node]){
                    ans++;
                    if(!visit[next.node]){
                        visit[next.node]=true;
                        q.add(next.node);
                    }
                }
            }
        }
        return ans;
    }
 
    private static int findShortPath() {
 
        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> o2.cost-o1.cost);
 
        pq.add(new Node(start,0));
        while (!pq.isEmpty()){
            Node cur = pq.poll();
            if(cur.cost < dist[cur.node]) continue;
 
            for (Node next : list.get(cur.node)) {
 
                if(dist[next.node] < dist[cur.node] + next.cost){
                    dist[next.node] = dist[cur.node] + next.cost;
                    pq.add(new Node(next.node, dist[next.node]));
                }
            }
        }
        return dist[end];
    }
 
    static class Node{
        int node,cost;
        public Node(int node, int cost) {
            this.node = node;
            this.cost = cost;
        }
    }
}