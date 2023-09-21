import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int N;
    static int[] tree, arr;
    static StringBuilder sb;
    static int Init(int treeIdx, int leftIdx, int rightIdx) {
        if (leftIdx == rightIdx) {
            tree[treeIdx] = arr[leftIdx];
            return tree[treeIdx];
        }
        int midIdx = (leftIdx + rightIdx) / 2;
        int leftValue = Init(treeIdx * 2, leftIdx, midIdx);
        int rightValue = Init(treeIdx * 2 + 1, midIdx + 1, rightIdx);

        tree[treeIdx] = Math.min(leftValue, rightValue);

        return tree[treeIdx];
    }

    static int Find(int treeIdx, int leftIdx, int rightIdx, int findLeftIdx, int findRightIdx) {
        if (leftIdx > findRightIdx || rightIdx < findLeftIdx) {
            return Integer.MAX_VALUE;
        }
        if (leftIdx >= findLeftIdx && rightIdx <= findRightIdx) {
            return tree[treeIdx];
        }
        int midIdx = (leftIdx + rightIdx) / 2;
        int leftValue = Find(treeIdx * 2, leftIdx, midIdx, findLeftIdx, findRightIdx);
        int rightValue = Find(treeIdx * 2 + 1, midIdx + 1 , rightIdx, findLeftIdx, findRightIdx);

        return Math.min(leftValue, rightValue);
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int k = 0;
        while ((int) Math.pow(2, k) < N) {
            k++;
        }
        tree = new int[(int) Math.pow(2, k + 1)];
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Init(1, 0, N - 1);
        sb = new StringBuilder();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            sb.append(Find(1, 0, N - 1, a - 1, b- 1)).append('\n');
        }
        System.out.println(sb.toString());
    }
}
