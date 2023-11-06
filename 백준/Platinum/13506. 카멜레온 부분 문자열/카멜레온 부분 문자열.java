import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb;
    static int[] pi;
    static int len, j, k, l, ans;

    public static void main(String[] args) throws IOException {
        sb = new StringBuilder();
        String str = br.readLine();
        len = str.length();
        pi = new int[len];
        j = 0;
        for (int i = 1; i < len; i++) {
            while(j > 0 && str.charAt(i) != str.charAt(j)) {
                j = pi[j - 1];
            }
            if (str.charAt(i) == str.charAt(j)) {
                pi[i] = ++j;
            }
        }

        l = pi[len - 1];
        k = 0;
        ans = 0;
        for (int i = 1; i < len - 1; i++) {
            while(k > 0 && str.charAt(i) != str.charAt(k)) {
                k = pi[k - 1];
            }
            if (str.charAt(i) == str.charAt(k)) {
                if (k == l - 1) {
                    ans = l;
                    break;
                } else {
                    k++;
                }
            }
        }
        if (ans > 0) {
            for (int i = 0; i < ans; i++) {
                sb.append(str.charAt(i));
            }
            System.out.println(sb);
        } else {
            if (l > 0) {
                pi = new int[l];
                j = 0;
                for (int i = 1; i < l; i++) {
                    while(j > 0 && str.charAt(i) != str.charAt(j)) {
                        j = pi[j - 1];
                    }
                    if (str.charAt(i) == str.charAt(j)) {
                        pi[i] = ++j;
                    }
                }
                ans = pi[l - 1];
            }
            if (ans == 0) {
                System.out.println(-1);
            } else {
                for (int i = 0; i < ans; i++) {
                    sb.append(str.charAt(i));
                }
                System.out.println(sb);
            }
        }
    }
}
