import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int[] heap;
    static int last;
    static void push(int x) {
        last++;
        heap[last] = x;
        int c = last;
        int p = c / 2;

        while(p != 0 && heap[p] > heap[c]) {
            int tmp = heap[c];
            heap[c] = heap[p];
            heap[p] = tmp;

            c = p;
            p = c / 2;
        }
    }

    static int pop() {
        int tmp = heap[1];
        heap[1] = heap[last--];
        int p = 1;
        int c = p * 2;

        while(c <= last) {
            if (c + 1 <= last && heap[c + 1] < heap[c]) {
                c = c + 1;
            }
            if (heap[c] < heap[p]) {
                int temp = heap[c];
                heap[c] = heap[p];
                heap[p] = temp;

            }
            p = c;
            c = p * 2;
        }
        return tmp;
    }


    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        heap = new int[100001];
        last = 0;
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            push(num);
        }
        int sumV = 0;
        while(last != 1) {
            int a = pop();
            int b = pop();
            int c = a + b;
            sumV += c;
            push(c);
        }
        System.out.println(sumV);
    }
}
