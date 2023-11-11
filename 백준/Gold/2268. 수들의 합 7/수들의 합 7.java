import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb;
    static int N, M, option, a, b;
    static int[] arr;
    static long[] segTree;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        int k = 0, tmp = 1;
        while(tmp < N) {
            tmp <<= 1;
            k++;
        }

        arr = new int[N + 1];
        segTree = new long[(int) Math.pow(2, k + 1)];
        sb = new StringBuilder();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            option = Integer.parseInt(st.nextToken());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            if (option == 0) {
                if (a > b) {
                    int t = a;
                    a = b;
                    b = t;
                }
                sb.append(findSeg(1, 1, N, a, b)).append('\n');
            } else {
                updateSeg(1, 1, N, a, b);
            }
        }
        System.out.println(sb);
    }
    static long findSeg(int treeIdx, int leftIdx, int rightIdx, int findLeftIdx, int findRightIdx) {
        if (leftIdx > findRightIdx || rightIdx < findLeftIdx) {
            return 0;
        }

        if (leftIdx >= findLeftIdx && rightIdx <= findRightIdx) {
            return segTree[treeIdx];
        }

        int midIdx = (leftIdx + rightIdx) / 2;
        long leftV = findSeg(treeIdx * 2, leftIdx, midIdx, findLeftIdx, findRightIdx);
        long rightV = findSeg(treeIdx * 2 + 1, midIdx + 1, rightIdx, findLeftIdx, findRightIdx);

        return leftV + rightV;
    }

    static void updateSeg(int treeIdx, int leftIdx, int rightIdx, int updateIdx, int updateV) {
        if (leftIdx == updateIdx && rightIdx == updateIdx) {
            segTree[treeIdx] = updateV;
            return;
        }
        if (leftIdx > updateIdx || rightIdx < updateIdx) {
            return;
        }
        int midIdx = (leftIdx + rightIdx) / 2;
        updateSeg(treeIdx * 2, leftIdx, midIdx, updateIdx, updateV);
        updateSeg(treeIdx * 2 + 1, midIdx + 1, rightIdx, updateIdx, updateV);
        segTree[treeIdx] = segTree[treeIdx * 2] + segTree[treeIdx * 2 + 1];
    }
}
