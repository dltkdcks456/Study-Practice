import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.TreeSet;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[] depth;
    static TreeSet<Integer> set;
    static int N, x;
    static long sumV;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        set = new TreeSet<>();
        depth = new int[N];
        sumV = 1;

        for (int i = 0; i < N; i++) {
            x = Integer.parseInt(br.readLine());
            if (set.isEmpty()) {
                set.add(x);
                depth[x] = 1;
                continue;
            }
            if (set.lower(x) == null) {
                depth[x] = depth[set.first()] + 1;
            } else {
                if (set.higher(x) == null) {
                    depth[x] = depth[set.lower(x)] + 1;
                } else {
                    depth[x] = Math.max(depth[set.lower(x)], depth[set.higher(x)]) + 1;
                }
            }
            sumV += depth[x];
            set.add(x);
        }
        System.out.println(sumV);
    }
}
