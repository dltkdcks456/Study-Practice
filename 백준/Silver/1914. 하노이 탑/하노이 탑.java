import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
    public void Hanoi(StringBuilder sb,  int N, int start, int mid, int des){ // N개가 start, mid, des 위치로 들어온다.
        if(N == 0) return;
        Hanoi(sb, N - 1, start, des, mid); // 가장 아래를 빼고 N - 1개는 위쪽 des로 가기 위해서 목적지를 가운데로 한다
        sb.append(start + " " + des + "\n"); // 가장 아래 원판을 des로 옮긴다
        Hanoi(sb,  N - 1, mid, start, des); // N - 1개가 가운데로 왔으니 des로 옮겨야 한다.
    }

    public static void main(String[] args) throws IOException {
        Main T = new Main();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        BigInteger minus = new BigInteger("1");
        BigInteger cnt = new BigInteger("2").pow(N).subtract(minus);

        if(N <= 20) {
            T.Hanoi(sb,  N, 1, 2, 3);
            System.out.println(cnt);
            System.out.println(sb);
        } else {
            System.out.println(cnt);
        }

    }
}
