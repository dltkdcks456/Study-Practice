import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int len;
    static int[] dp;
    public static void main(String[] args) throws IOException {
        while(true) {
            String str = br.readLine().trim();
            if (str.equals(".")) break;
            int len = str.length();
            dp = new int[len];
            int j = 0;
            for (int i = 1; i < len; i++) {
                while(j > 0 && str.charAt(i) != str.charAt(j)) {
                    j = dp[j - 1];
                }
                if (str.charAt(i) == str.charAt(j)) {
                    dp[i] = ++j;
                }

            }

            int N = dp[len - 1] - 1;
            long cnt = 0;
            for (int i = 0; i <= N; i++) {
                if ((len % (i + 1)) != 0) continue;
                int k = 0;
                boolean flag = true;
                for (int l = 0; l < len; l++) {
                    while(str.charAt(l) != str.charAt(k)) {
                        flag = false;
                        cnt = 0;
                        break;
                    }
                    if (str.charAt(l) == str.charAt(k)) {
                        if (k == i) {
                            cnt++;
                            k = 0;
                        } else {
                            k++;
                        }
                    }
                    if (!flag) break;
                }
                if (cnt > 0) break;
            }


            if (cnt == 0) {
                System.out.println(1);
            } else {
                System.out.println(cnt);
            }


        }


    }
}

