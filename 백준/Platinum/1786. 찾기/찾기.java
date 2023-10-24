import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb;
    static int[] table;

    public static void main(String[] args) throws IOException {
        String T = br.readLine();
        String P = br.readLine();

        int patterLen = P.length();

        failure(P, patterLen);

        int totalLen = T.length();
        int k = 0, cnt = 0;
        ArrayList<Integer> arr = new ArrayList<>();
        sb = new StringBuilder();
        for (int i = 0; i < totalLen; i++) {
            while (k > 0 && (T.charAt(i) != P.charAt(k))) {
                k = table[k - 1];
            }
            if (T.charAt(i) == P.charAt(k)) {
                if (k == patterLen - 1) {
                    k = table[k];
                    cnt++;
                    sb.append(i + 1 - (patterLen - 1)).append(" ");
                } else {
                    k++;
                }
            }
        }
        sb.insert(0, cnt + "\n");
        System.out.println(sb);
    }

    static void failure(String str, int L) {
        table = new int[L];
        int j = 0;
        for (int i = 1; i < L; i++) {
            while(j > 0 && (str.charAt(i) != str.charAt(j))) {
                j = table[j - 1];
            }
            if (str.charAt(i) == str.charAt(j)) {
                table[i] = ++j;
            }
        }
    }
}
