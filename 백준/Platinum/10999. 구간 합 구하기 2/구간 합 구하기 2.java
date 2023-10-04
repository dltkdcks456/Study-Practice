import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static long[] lazy, tree, arr;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int k = 0, tmp = 1;
        while (tmp < N) {
            tmp <<= 1;
            ++k;
        }

        tree = new long[(int) Math.pow(2, k + 1)];
        lazy = new long[(int) Math.pow(2, k + 1)];
        arr = new long[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Long.parseLong(br.readLine());
        }

        initSeg(1, 0, N - 1);

        for (int i = 0; i < M + K; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            if (a == 1) {
                long d = Long.parseLong(st.nextToken());
                updateSeg(1, 0, N - 1, b - 1, c - 1, d);
            } else {
                System.out.println(pSum(1, 0, N - 1, b - 1, c - 1));
            }
        }
    }

    static long initSeg(int treeIdx, int leftIdx, int rightIdx) {
        if (leftIdx == rightIdx) {
            return tree[treeIdx] = arr[leftIdx];
        }
        int midIdx = (leftIdx + rightIdx) / 2;

        return tree[treeIdx] = initSeg(treeIdx * 2, leftIdx, midIdx) + initSeg(treeIdx * 2 + 1, midIdx + 1, rightIdx);

    }

    static void updateSeg(int treeIdx, int leftIdx, int rightIdx, int updateLeftIdx, int updateRightIdx, long diff) {
        propagate(treeIdx, leftIdx, rightIdx);
        if (leftIdx > updateRightIdx || rightIdx < updateLeftIdx) {
            return;
        }
        if (leftIdx >= updateLeftIdx && rightIdx <= updateRightIdx) {
            lazy[treeIdx] = diff;
            propagate(treeIdx, leftIdx, rightIdx);
            return;
        }

        int midIdx = (leftIdx + rightIdx) / 2;
        updateSeg(treeIdx * 2, leftIdx, midIdx, updateLeftIdx, updateRightIdx, diff);
        updateSeg(treeIdx * 2 + 1, midIdx + 1, rightIdx, updateLeftIdx, updateRightIdx, diff);

        tree[treeIdx] = tree[treeIdx * 2] + tree[treeIdx * 2 + 1];
    }

    static void propagate(int treeIdx, int leftIdx, int rightIdx) {
        if (lazy[treeIdx] != 0) {
            if (leftIdx != rightIdx) {
                lazy[treeIdx * 2] += lazy[treeIdx];
                lazy[treeIdx * 2 + 1] += lazy[treeIdx];
            }
            tree[treeIdx] += lazy[treeIdx] * (rightIdx - leftIdx + 1);
            lazy[treeIdx] = 0;
        }
    }

    static long pSum(int treeIdx, int leftIdx, int rightIdx, int leftFindIdx, int rightFindIdx) {
        propagate(treeIdx, leftIdx, rightIdx);
        if (leftIdx > rightFindIdx || rightIdx < leftFindIdx) {
            return 0;
        }
        if (leftIdx >= leftFindIdx && rightIdx <= rightFindIdx) {
            return tree[treeIdx];
        }

        int midIdx = (leftIdx + rightIdx) / 2;
        long leftValue = pSum(treeIdx * 2, leftIdx, midIdx, leftFindIdx, rightFindIdx);
        long rightValue = pSum(treeIdx * 2 + 1, midIdx + 1, rightIdx, leftFindIdx, rightFindIdx);

        return leftValue + rightValue;
    }

}
