import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb;
    static int N, cnt, prevNum;
    static int[][] memo;
    static int[] arr, visited;

    public static void main(String[] args) throws IOException {
        sb = new StringBuilder();
        memo = new int[101][101];
        for (int i = 1; i <= 100; i++) {
            for (int j = 1; j <= 100; j++) {
                memo[i][j] = gcd(i, j);
            }
        }
        while(true) {
            N = Integer.parseInt(br.readLine());
            if (N == 0) break;
            arr = new int[N];
            for (int i = 0; i < N; i++) {
                arr[i] = Integer.parseInt(br.readLine());
            }
            cnt = 0;
            visited = new int[101];
            prevNum = 0;
            for (int i = 1; i <= 100; i++) {
                for (int j = 0; j < N; j++) {
                    if (arr[j] == i) {
                        if (visited[i] == 0) {
                            visited[i] = 1;
                            cnt++;
                            break;
                        } else {
                            break;
                        }
                    }
                    if (j == 0) {
                        prevNum = arr[j];
                        continue;
                    }
                    prevNum = memo[prevNum][arr[j]];
                    if (prevNum % i == 0) {
                        if (prevNum == i) {
                            if (visited[i] == 0) {
                                visited[i] = 1;
                                cnt++;
                                break;
                            } else {
                                break;
                            }
                        }
                    } else {
                        prevNum = arr[j];
                    }
                }
            }
            sb.append(cnt).append('\n');
        }
        System.out.println(sb);
    }

    static int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }
}
