import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        p_1158();
    }

    /**
     * 2023/07/29-> 3, 구현
     */
    static void p_1158() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer tk = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(tk.nextToken());
        int K = Integer.parseInt(tk.nextToken()) - 1;

        List<Integer> list = new ArrayList<>();
        for (int i = 1; i <= N; i++) {
            list.add(i);
        }

        sb.append("<");
        int idx = 0;
        for (int i = 0; i < N; i++) {
            idx += K;

            if(idx >= list.size()) idx %= list.size();

            Integer num = list.remove(idx);
            sb.append(num);
            if(i < N-1) sb.append(", ");
        }

        sb.append(">");
        System.out.println(sb);
    }
}