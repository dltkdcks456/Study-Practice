import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb;
    static int last;
    static int[] heap;
    static void push(int x) {
        last++;
        heap[last] = x;
        int c = last;
        int p = c / 2;
        while(p != 0 && heap[p] > heap[c]) {
            swap(p, c);
            c = p;
            p = c / 2;
        }
    }

    static int pop() {
        if (last == 0) {
            return 0;
        }
        int temp = heap[1];
        swap(1, last);
        last--;
        int p = 1;
        int c = p * 2;
        while(c <= last) {
            if (c + 1 <=last && heap[c] > heap[c + 1]) {
                c++;
            }
            if (heap[c] < heap[p]) {
                swap(p, c);
                p = c;
                c = p * 2;
            } else {
                break;
            }
        }
        return temp;
    }

    static void swap(int a, int b) {
        int tmp = heap[a];
        heap[a] = heap[b];
        heap[b] = tmp;
    }

    public static void main(String[] args) throws IOException {
        sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        last = 0;
        heap = new int[N + 1];
        for (int i = 0; i < N; i++) {
            int x = Integer.parseInt(br.readLine());
            if (x != 0) {
                push(x);
            } else {
                sb.append(pop()).append('\n');
            }
        }
        System.out.println(sb.toString());

    }
}
