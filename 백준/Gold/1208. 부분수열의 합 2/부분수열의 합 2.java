import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static ArrayList<Long> arr, sumArr1, sumArr2;
    static long[] arr1, arr2;
    static boolean[] visited;
    static int N;
    static long cnt, S;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        S = Long.parseLong(st.nextToken());
        arr = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            long inputNum = Integer.parseInt(st.nextToken());
            arr.add(inputNum);
        }

        int len = arr.size();
        int m = len / 2;
        sumArr1 = new ArrayList<>();
        sumArr2 = new ArrayList<>();
        arr1 = new long[m];
        arr2 = new long[len - m];
        for (int i = 0; i < m; i++) {
            arr1[i] = arr.get(i);
        }
        for (int i = 0; i < len - m; i++) {
            arr2[i] = arr.get(i + m);
        }

        cnt = 0;

        visited = new boolean[m];
        for (int i = 1; i < m + 1; i++) {
            comb(arr1, sumArr1, 0, 0, 0, i);
        }

        visited = new boolean[len - m];
        for (int i = 1; i < len - m + 1; i++) {
            comb(arr2, sumArr2, 0, 0, 0, i);
        }

        Collections.sort(sumArr1);
        Collections.sort(sumArr2);

        int l = 0;
        int r = sumArr2.size() - 1;

        while(l < sumArr1.size() && r >= 0) {
            long sumV = sumArr1.get(l) + sumArr2.get(r);
            if (sumV == S) {
                long a = sumArr1.get(l);
                long cnt1 = 0;
                while(l < sumArr1.size() && sumArr1.get(l) == a) {
                    l++;
                    cnt1++;
                }

                long b = sumArr2.get(r);
                long cnt2 = 0;
                while(r >= 0 && sumArr2.get(r) == b) {
                    r--;
                    cnt2++;
                }
                cnt += cnt1 * cnt2;

            } else if (sumV < S) {
                l++;
            } else {
                r--;
            }
        }

        System.out.println(cnt);
    }
    static void comb(long[] tmpArr, ArrayList<Long> tmpList , int idx, int depth, long sumV, int des) {
        if (depth == des) {
            tmpList.add(sumV);
            if (sumV == S) {
                cnt++;
            }
            return;
        }
        for (int i = idx; i < tmpArr.length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                sumV += tmpArr[i];
                comb(tmpArr, tmpList, i, depth + 1, sumV, des);
                sumV -= tmpArr[i];
                visited[i] = false;
            }
        }
    }
}
