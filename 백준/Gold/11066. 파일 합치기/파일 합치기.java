import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int INF = 500000000;
	static int[][] dp;
	static int[] arr;
	
	public static void main(String[] args) throws IOException {
		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			int N = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			dp = new int[N][N];
			arr = new int[N + 1];
			
			for (int i = 1; i < N; i++) {
				for (int j = i - 1; j > -1; j--) {
					dp[j][i] = INF;
				}
			}
			
			for (int i = 0; i < N; i++) {
				arr[i + 1] = Integer.parseInt(st.nextToken());
			}
			
			for (int i = 2; i < N + 1; i++) {
				arr[i] += arr[i - 1];
				
			}
			
			for (int r = 1; r < N; r++) {
				for (int c = 0; c + r < N; c++) {
					for (int k = c; k < r + c; k++) {
						dp[c][r + c] = Math.min(dp[c][r + c], dp[c][k] + dp[k + 1][r + c] + arr[r + c + 1] - arr[c]);						
					}
				}
			}
			
			System.out.println(dp[0][N - 1]);
			
		}
	}
}
