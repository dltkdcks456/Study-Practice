import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static HashMap<Long, Long> map;
    static long ans;

    public static void main(String[] args) throws IOException {
        long N = Long.parseLong(br.readLine());
        if (N == 1) {
            System.out.println(1);
        }
        else if (isPrime(N)) {
            System.out.println(N - 1);
        } else {
            map = new HashMap<>();
            long tmp = N;
            for (int i = 2; (long) i * i <= N; i++) {
                while(tmp % i == 0) {
                    tmp /= i;
                    map.put((long) i, map.getOrDefault((long) i, 1L) * i);
                }
            }
            if (tmp != 1) {
                map.put(tmp, tmp);
            }

            ans = 1;
            for (long key : map.keySet()) {
                if (key == map.get(key)) {
                    ans *= (map.get(key) - 1);
                } else {
                    ans = ans * map.get(key) * (key - 1) / key ;
                }
            }
            System.out.println(ans);
        }
    }

    static boolean isPrime(long x) {
        if (x <= 1) return false;
        for (int i = 2; (long) i * i <= x; i++) {
            if (x % i == 0) {
                return false;
            }
        }
        return true;
    }
}
