import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb;
    static HashMap<Integer, ArrayList<Integer>> arr;

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        arr = new HashMap<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if (arr.containsKey(a)) {
                arr.get(a).add(b);
            } else {
                ArrayList<Integer> tmp = new ArrayList<>();
                tmp.add(b);
                arr.put(a, tmp);
            }
            if (arr.containsKey(b)) {
                arr.get(b).add(a);
            } else {
                ArrayList<Integer> tmp = new ArrayList<>();
                tmp.add(a);
                arr.put(b, tmp);
            }
        }

        for (int key : arr.keySet()) {
            ArrayList<Integer> list = arr.get(key);
            Collections.sort(list);
        }

        int Q = Integer.parseInt(br.readLine());
        sb = new StringBuilder();
        for (int i = 0; i < Q; i++) {
            int ans = -1;
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            // 시작점 탐색
            ArrayList<Integer> startPoint = arr.get(a);
            ArrayList<Integer> endPoint = arr.get(b);

            if (!(startPoint == null || endPoint == null)) {
                boolean startFlag = false;
                int s = 0, e = startPoint.size() - 1;
                int target = 0;
                while(s <= e) {
                    int m = (s + e) / 2;
                    if (startPoint.get(m) == b) {
                        ans = 1;
                        break;
                    } else if (startPoint.get(m) > b) {
                        e = m - 1;
                    } else {
                        s = m + 1;
                    }
                }
                if (ans != 1) {
                    if (s < startPoint.size()) {
                        target = startPoint.get(s);
                    } else {
                        target = startPoint.get(e);
                    }

                    if (target > b) {
                        startFlag = true;
                    }
                }

                s = 0;
                e = endPoint.size() - 1;
                target = 0;
                boolean endFlag = false;
                while(s <= e && ans != 1) {
                    int m = (s + e) / 2;
                    if (endPoint.get(m) == a) {
                        ans = 1;
                        break;
                    } else if (endPoint.get(m) > a) {
                        e = m - 1;
                    } else {
                        s = m + 1;
                    }
                }
                if (ans != 1) {
                    if (e >= 0) {
                        target = endPoint.get(e);
                    } else {
                        target = endPoint.get(s);
                    }

                    if (target < a) {
                        endFlag = true;
                    }
                }

                if (startFlag && endFlag) {
                    ans = 2;
                }
            }
            sb.append(ans).append('\n');
        }
        System.out.println(sb.toString());
    }
}
