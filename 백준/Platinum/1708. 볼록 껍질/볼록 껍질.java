import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static List<Point> points;
    static class Point {
        // 곱셈이 들어가므로 x, y를 long으로 진행
        long x;
        long y;
        public Point(long x, long y) {
            this.x = x;
            this.y = y;
        }
    }

    static int ccw(Point A, Point B, Point C) {
        // 외적을 통해 시계, 반시계 방향 회전 감지
        long result = (long) (B.x - A.x) * (C.y - A.y) - (long) (B.y - A.y) * (C.x - A.x);
        if (result > 0) return 1; // 반시계
        else if (result < 0) return -1; // 시계
        else return 0; // 일직선
    }

    static long dist(Point A, Point B) {
        // 곱셈이 있으므로 타입을 long으로 반드시 해주기!!
        return (A.x - B.x) * (A.x - B.x) + (A.y - B.y) * (A.y - B.y);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        points = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            long x = Long.parseLong(st.nextToken());
            long y = Long.parseLong(st.nextToken());
            points.add(new Point(x, y));
        }
        // y 및 x값이 가장 작은 좌표 찾기(기준점 선정)
        for (int i = 1; i < N; i++) {
            // y값이 작고, 만약 같은 경우 x가 작은 것으로 swap 진행 -> 인덱스 0이 기준점이 되도록 만든다.
            if (points.get(0).y > points.get(i).y || (points.get(0).y == points.get(i).y && points.get(0).x > points.get(i).x)) {
                Point tmp = points.get(0);
                points.set(0, points.get(i));
                points.set(i, tmp);
            }
        }

        // 반시계 방향으로 정렬 진행
        Collections.sort(points, new Comparator<Point>() {
            @Override
            public int compare(Point o1, Point o2) {
                Point origin = points.get(0);
                int check = ccw(origin, o1, o2);
                if (check > 0) return -1; // 반시계이므로 그대로
                else if (check < 0) return 1; // 시계이므로 정렬
                else { // 일직선일 경우 가까운 거리를 채택
                    long distA = dist(origin, o1);
                    long distB =  dist(origin, o2);
                    if (distA > distB) return 1; // 거리가 더 멀면 바꾼다.
                    else return -1;
                }
            }
        });

        Stack<Integer> stack = new Stack<>();
        stack.push(0);
        for (int i = 1; i < N; i++) {
            // stack에 각 지점들을 넣어두고 3개의 점을 통해 ccw를 확인 -> 반시계 방향만 넣어주고 나머지는 pop
            while(stack.size() > 1 && ccw(points.get(stack.get(stack.size() - 2)), points.get(stack.peek()), points.get(i)) <= 0) stack.pop();
            stack.push(i);
        }
        bw.write(String.valueOf(stack.size()));
        bw.flush();
        bw.close();
    }
}
