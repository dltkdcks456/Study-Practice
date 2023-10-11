import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static HashMap<Long, ArrayList<Integer>> words;
    static int prime = 1_000_000_007;
    static long[] multiply;

    public static void main(String[] args) throws IOException {
        int L = Integer.parseInt(br.readLine());
        multiply = new long[L + 1];
        multiply[0] = 1;
        for (int i = 1; i < L + 1; i++) {
            multiply[i] = (multiply[i - 1] * 27) % prime;
        }
        String str = br.readLine();
        int start = 1, end = L, ans = 0;
        while(start <= end) {
            int mid = (start + end) / 2;
            if (check(str, mid)) {
                start = mid + 1;
                if (mid > ans) {
                    ans = mid;
                }
            } else {
                end = mid - 1;
            }
        }
        System.out.println(ans);
    }

    static boolean check(String str, int L) {
        words = new HashMap<>();
        long hash = createHash(str, L);

        ArrayList<Integer> wordMap = new ArrayList<>();
        wordMap.add(0);
        words.put(hash, wordMap);

        for (int i = L; i < str.length(); i++) {
            boolean flag = true;
            hash = (long) (hash - (((str.charAt(i - L) - 96) * multiply[L - 1] % prime))) % prime;
            hash = (hash * 27) % prime;
            hash = hash + str.charAt(i) - 96;
            if (hash < 0) {
                hash += prime;
            }

            if (words.containsKey(hash)) {
                for (int idx : words.get(hash)) {
                    for (int j = 0; j < L; j++) {
                        if (str.charAt(idx + j) != str.charAt(i - L + 1 + j)) {
                            flag = false;
                        }
                    }
                }
            } else {
                ArrayList<Integer> newWordMap = new ArrayList<>();
                newWordMap.add(i - L + 1);
                words.put(hash, newWordMap);
                flag = false;
            }
            if (flag) return true;
        }
        return false;
    }

    static long createHash(String str, int L) {
        long tmp = 0;
        for (int i = 0; i < L; i++) {
            tmp = (tmp * 27) % prime;
            tmp += str.charAt(i) - 96;
        }
        return tmp;
    }

}

