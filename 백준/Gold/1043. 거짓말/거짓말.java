import java.io.*;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.StringTokenizer;

public class Main {
    public static int[] parents;
    public static int cnt;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        cnt = 0;
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        parents = new int[N + 1];
        for (int i = 1; i < N + 1; i++) {
            parents[i] = i;
        }
        int knownum = Integer.parseInt(st.nextToken());
        int[] knowPeople = new int[knownum];
        ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            arr.add(new ArrayList<Integer>());
        }
        if (knownum != 0) {
            for (int i = 0; i < knownum; i++) {
                knowPeople[i] = (Integer.parseInt(st.nextToken()));
            }
            for (int i = 1; i < knownum ; i++) {
                union(knowPeople[0], knowPeople[i]);
            }

            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine());
                int partyNum = Integer.parseInt(st.nextToken());
                for (int j = 0; j < partyNum; j++) {
                    arr.get(i).add(Integer.parseInt(st.nextToken()));
                }

                for (int j = 1; j < partyNum; j++) {
                    union(arr.get(i).get(0), arr.get(i).get(j));
                }
            }
            for (int i = 0; i < M; i++) {
                boolean flag = true;
                for (int j = 0; j < arr.get(i).size(); j++) {

                    if (find(arr.get(i).get(j)) == find(knowPeople[0])) {
                        flag = false;
                        break;
                    }
                }

                if (flag) {
                    cnt++;
                }
            }
            bw.write(String.valueOf(cnt));
            bw.flush();
            bw.close();

        } else {
            bw.write(String.valueOf(M));
            bw.flush();
            bw.close();
        }

    }
    public static int find(int x) {
        if (parents[x] == x) {
            return x;
        }
        return parents[x] = find(parents[x]);
    }
    public static void union(int a, int b) {
        int A = find(a);
        int B = find(b);
        parents[B] = A;
    }
}
