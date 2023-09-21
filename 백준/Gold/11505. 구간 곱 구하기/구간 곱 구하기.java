import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int N, M, K;
    static StringTokenizer st;
    static StringBuilder sb;
    static final long Num = 1000000007;
    static long[] tree;
    static int[] arr;

    static long Init(int treeIdx, int leftIdx, int rightIdx) {
        if (leftIdx == rightIdx) {
            tree[treeIdx] = arr[leftIdx];
            return tree[treeIdx];
        }
        int midIdx = (leftIdx + rightIdx) / 2;
        long leftValue = Init(treeIdx * 2, leftIdx, midIdx);
        long rightValue = Init(treeIdx * 2 + 1, midIdx + 1, rightIdx);
        tree[treeIdx] = (leftValue * rightValue) % Num;

        return tree[treeIdx];
    }

    static long Update(int treeIdx, int leftIdx, int rightIdx, int updateIdx, int updateValue) {
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
        tree[treeIdx] = (leftValue * rightValue) % Num;

        return tree[treeIdx];
    }

    static long Find(int treeIdx, int leftIdx, int rightIdx, int findLeftIdx, int findRightIdx) {
        if (leftIdx > findRightIdx || rightIdx < findLeftIdx) {
            return 1;
        }
        if (leftIdx >= findLeftIdx && rightIdx <= findRightIdx) {
            return tree[treeIdx];
        }
        int midIdx = (leftIdx + rightIdx) / 2;
        long leftValue = Find(treeIdx * 2, leftIdx, midIdx, findLeftIdx, findRightIdx);
        long rightValue = Find(treeIdx * 2 + 1, midIdx + 1, rightIdx, findLeftIdx, findRightIdx);

        return (leftValue * rightValue) % Num;
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        int k = 0;
        while(Math.pow(2, k) < N) {
            ++k;
        }
        tree = new long[(int) Math.pow(2, k + 1)];
        arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Init(1, 0, N - 1);

        sb = new StringBuilder();
        for (int i = 0; i < M + K; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            if (a == 1) {
                Update(1, 0, N - 1, b - 1, c);
            } else {
                long tmp = Find(1, 0, N - 1, b - 1, c - 1);
                sb.append(tmp).append('\n');
            }
        }
        System.out.println(sb.toString());
    }
}
