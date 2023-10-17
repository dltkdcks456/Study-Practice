import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;
class Main
{
    static List<Point> points;
    static class Point implements Comparable<Point>{
        @Override
        public int compareTo(Point o) {
            if (this.x > o.x) {
                return 1;
            } else if (this.x < o.x) {
                return -1;
            } else {
                return 0;
            }

        }
        long x;
        long y;
        public Point(long x, long y) {
            this.x = x;
            this.y = y;
        }
    }
    static class PointComparator implements Comparator<Point> {

        @Override
        public int compare(Point o1, Point o2) {
            if (o1.y > o2.y) {
                return 1;
            } else if (o1.y < o2.y) {
                return -1;
            } else {
                return 0;
            }
        }

    }
    static long dist(Point a, Point b) {
        return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
    }
    static long bruteForce(List<Point> a, int x, int y) {
        long ans = -1;
        for (int i = x; i <= y - 1; i++) {
            for (int j = i + 1; j <= y;j++) {
                long tmp = dist(points.get(i), points.get(j));
                if (ans == -1 || ans > tmp) {
                    ans = tmp;
                }
            }
        }
        return ans;
    }
    static long closest(List<Point> a, int x, int y) {
        int tmp = y - x + 1;
        if (tmp <= 3) {
            return bruteForce(a, x, y);
        }

        int mid = (x + y) / 2;
        long left = closest(a, x, mid);
        long right = closest(a, mid + 1, y);
        long ans = Math.min(left, right);

        ArrayList<Point> b = new ArrayList<>();

        for(int i = x; i <= y; i++) {
            long d = points.get(i).x - points.get(mid).x;
            if (d * d < ans) {
                b.add(points.get(i));
            }
        }

        Collections.sort(b, new PointComparator());

        int m = b.size();
        for(int i = 0; i < m - 1; i++) {
            for(int j = i + 1; j < m; j++) {
                long k = b.get(j).y - b.get(i).y;
                if (k * k < ans) {
                    long d = dist(b.get(i), b.get(j));
                    if (d < ans) {
                        ans = d;
                    }
                }
                else {
                    break;
                }
            }
        }
        return ans;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        points = new ArrayList<>();
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            long a = Integer.parseInt(st.nextToken());
            long b = Integer.parseInt(st.nextToken());
            points.add(new Point(a, b));
        }
        Collections.sort(points);
        long result = closest(points, 0, N - 1);
        bw.write(result + "\n");

        bw.flush();
        bw.close();
    }
}
