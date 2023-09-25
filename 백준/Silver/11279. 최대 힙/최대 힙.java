import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int N, last;
    static int[] heap;

    static void push(int x) {
        last++;
        heap[last] = x;
        int c = last;
        int p = c / 2;

        while(p != 0 && heap[p] < heap[c]) {
            int tmp = heap[c];
            heap[c] = heap[p];
            heap[p] = tmp;
            c = p;
            p = c / 2;
        }
    }

    static int pop(){
        if (last == 0) {
            return 0;
        }
        int temp = heap[1];
        heap[1] = heap[last];
        last--;

        int p = 1;
        int c = 2 * p;
        while (c <= last) {
            if (c + 1 <= last && heap[c] < heap[c + 1]) {
                c += 1;
            }
            if (heap[p] < heap[c]) {
                int tmp = heap[p];
                heap[p] = heap[c];
                heap[c] = tmp;
                p = c;
                c = p * 2;
            } else {
                break;
            }
        }

        return temp;
    }

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        last = 0;
        heap = new int[100001];
        for (int i = 0; i < N; i++) {
            int x = Integer.parseInt(br.readLine());
            if (x != 0) {
                // push
                push(x);
            } else {
                // pop
                System.out.println(pop());
            }
        }
    }
}
