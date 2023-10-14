import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb;
    static long[] segTree, lazy;
    static int[] arr;
    static int N;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());

        int k = 0, tmp = 1;
        while(tmp < N) {
            tmp <<= 1;
            k++;
        }

        segTree = new long[(int) Math.pow(2, k + 1)];
        lazy = new long[(int) Math.pow(2, k + 1)];

        arr = new int[N];
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        initSeg(1, 0, N - 1);

        int M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int option = Integer.parseInt(st.nextToken());
            if (option == 1) {
                updateSeg(1, 0, N - 1, Integer.parseInt(st.nextToken()) - 1, Integer.parseInt(st.nextToken()) - 1, Integer.parseInt(st.nextToken()));
            } else {
                System.out.println(findSeg(1, 0, N - 1, Integer.parseInt(st.nextToken()) - 1));
            }
        }


    }

    static void initSeg(int treeIdx, int leftIdx, int rightIdx) {
        if (leftIdx == rightIdx) {
            segTree[treeIdx] = arr[leftIdx];
            return;
        }
        int midIdx = (leftIdx + rightIdx) / 2;
        initSeg(treeIdx * 2, leftIdx, midIdx);
        initSeg(treeIdx * 2 + 1, midIdx + 1, rightIdx);
    }

    static void propagate(int treeIdx, int leftIdx, int rightIdx) {
        if (lazy[treeIdx] != 0) {
            if (leftIdx != rightIdx) {
                lazy[treeIdx * 2] += lazy[treeIdx];
                lazy[treeIdx * 2 + 1] += lazy[treeIdx];
            } else {
                segTree[treeIdx] += lazy[treeIdx];
            }
            lazy[treeIdx] = 0;
        }
    }

    static void updateSeg(int treeIdx, int leftIdx, int rightIdx, int updateLeftIdx, int updateRightIdx, int diff) {
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
    }

    static long findSeg(int treeIdx, int leftIdx, int rightIdx, int findIdx) {
        propagate(treeIdx, leftIdx, rightIdx);
        if (leftIdx > findIdx || rightIdx < findIdx) {
            return 0;
        }
        if (leftIdx == findIdx && rightIdx == findIdx) {
            return segTree[treeIdx];
        }
        int midIdx = (leftIdx + rightIdx) / 2;
        long leftV = findSeg(treeIdx * 2, leftIdx, midIdx, findIdx);
        long rightV = findSeg(treeIdx * 2 + 1, midIdx + 1, rightIdx, findIdx);

        return leftV + rightV;
    }
}
