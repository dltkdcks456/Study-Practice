import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static long[] tree, li;
    
    static long Init(int treeIdx, int leftIdx, int rightIdx) {
        if (leftIdx == rightIdx) {
            tree[treeIdx] = li[leftIdx];
            return tree[treeIdx];
        }

        int midIdx = (leftIdx + rightIdx) / 2;
        long leftValue = Init(treeIdx * 2, leftIdx, midIdx);
        long rightValue = Init(treeIdx * 2 + 1, midIdx + 1, rightIdx);
        tree[treeIdx] = leftValue + rightValue;
        return tree[treeIdx];
    }

    static long Find(int treeIdx, int leftIdx, int rightIdx, int FindLeftIdx, int FindRightIdx) {
        if (leftIdx > FindRightIdx || rightIdx < FindLeftIdx) {
            return 0;
        }
        if (leftIdx >= FindLeftIdx && rightIdx <= FindRightIdx) {
            return tree[treeIdx];
        }

        int midIdx = (leftIdx + rightIdx) / 2;

        long LeftValue = Find(treeIdx * 2, leftIdx, midIdx, FindLeftIdx, FindRightIdx);
        long RightValue = Find(treeIdx * 2 + 1, midIdx + 1, rightIdx, FindLeftIdx, FindRightIdx);

        return LeftValue + RightValue;
    }

    static long Update(int treeIdx, int leftIdx, int rightIdx, int updateIdx, long updateValue) {
        if (leftIdx > updateIdx || rightIdx < updateIdx) {
            return tree[treeIdx];
        }
        if (leftIdx == updateIdx && rightIdx == updateIdx) {
            tree[treeIdx] = updateValue;
            return tree[treeIdx];
        }
        int midIdx = (leftIdx + rightIdx) / 2;
        long leftValue = Update(treeIdx * 2, leftIdx, midIdx, updateIdx, updateValue);
        long rightValue = Update(treeIdx * 2 + 1, midIdx + 1, rightIdx, updateIdx, updateValue);
        tree[treeIdx] = leftValue + rightValue;

        return tree[treeIdx];
    }

    public static void main(String[] args) throws IOException {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());
            int k = 0;
            while ((int) (Math.pow(2, k)) < N) {
                k++;
        }
            tree = new long[(int) Math.pow(2, k + 1)];
            li = new long[N];
            for (int i = 0; i < N; i++) {
                li[i] = Long.parseLong(br.readLine());
            }
            Init(1, 0, N - 1);

        for (int i = 0; i < M + K; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            long c = Long.parseLong(st.nextToken());
            if (a == 1) {
                Update(1, 0, N - 1, b - 1, c);
            } else {
                System.out.println(Find(1, 0, N - 1, b - 1, (int) c - 1));
            }
        }
    }
}
