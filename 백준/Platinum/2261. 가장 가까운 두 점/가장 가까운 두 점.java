import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[][] xarr;
    static int n, minV;

    static void closest(int s, int e) {
        int tmp = e - s + 1;
        if (tmp <= 3) {
            getMinDistance(s, e);
            return;
        }
        int m = (s + e) / 2;
        closest(s, m - 1);
        closest(m + 1, e);

        ArrayList<int[]> b = new ArrayList<>();


        for (int i = s; i <= e; i++) {
            int dt = (xarr[m][0] - xarr[i][0]) * (xarr[m][0] - xarr[i][0]);
            if (dt < minV) {
                b.add(xarr[i]);
            }
        }

        Comparator<int[]> cmpY = (o1, o2) -> o1[1] - o2[1];
        b.sort(cmpY);

        for (int i = 0; i < b.size() - 1; i++) {
            for (int j = i + 1; j < b.size(); j++) {
                int dy = Math.abs(b.get(i)[1] - b.get(j)[1]);
                if (dy * dy < minV) {
                    int dt = getDistance(b.get(i), b.get(j));
                    if (dt < minV) {
                        minV = dt;
                    }
                } else {
                    break;
                }
            }
        }

    }

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        xarr = new int[n][2];
        minV = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            xarr[i] = new int[] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
        }

        Comparator<int[]> cmpX = new Comparator<int[]>() {

            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        };

        Arrays.sort(xarr, cmpX);

        closest(0, n - 1);
        System.out.println(minV);
    }

    static void getMinDistance(int s, int e) {
        for (int i = s; i <= e - 1; i++) {
            for (int j = i + 1; j <= e; j++) {
                int d = getDistance(xarr[i], xarr[j]);
                if (d < minV) {
                    minV = d;
                }
            }
        }
    }

    static int getDistance(int[] a, int[] b) {
        return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]);
    }
}
