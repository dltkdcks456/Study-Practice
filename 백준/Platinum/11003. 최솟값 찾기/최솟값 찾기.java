import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb;
    static Deque<int[]> deque;
    static int N, L;
    
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        sb = new StringBuilder();
        deque = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            int tmp = Integer.parseInt(st.nextToken());
            while(!deque.isEmpty() && deque.getLast()[0] > tmp) {
                deque.pollLast();
            }
            deque.addLast(new int[] {tmp, i});
            if (deque.getFirst()[1] == i - L) {
                deque.pollFirst();
            }
            sb.append(deque.getFirst()[0]).append(" ");
        }
        System.out.println(sb);
    }
}
