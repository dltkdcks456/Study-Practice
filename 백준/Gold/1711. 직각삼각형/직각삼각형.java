import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[][] coor;

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        coor = new int[N][2];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            coor[i] = new int[] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
        }

        int cnt = 0;


        for (int i = 0; i < N; i++) {
            HashMap<ArrayList<Integer>, Integer> m = new HashMap<>();
            for (int j = 0; j < N; j++) {
                if (i == j) continue;
                int x = coor[i][0] - coor[j][0];
                int y = coor[i][1] - coor[j][1];
                int g = gcd(x, y);
                if (g < 0) {
                    g = -g;
                }
                x /= g;
                y /= g;
                ArrayList<Integer> key = new ArrayList<>();
                key.add(x);
                key.add(y);
                m.put(key, m.getOrDefault(key, 0) + 1);
            }

            for (ArrayList<Integer> point : m.keySet()) {
                ArrayList<Integer> tmp = new ArrayList<>();
                tmp.add(-point.get(1));
                tmp.add(point.get(0));

                cnt += m.get(point) * m.getOrDefault(tmp, 0);
            }
        }
        System.out.println(cnt);
    }

    static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

}
