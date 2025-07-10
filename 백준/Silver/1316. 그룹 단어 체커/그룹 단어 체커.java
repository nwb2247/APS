import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int cnt = N;
        for (int n=0; n<N; n++) {

            char[] chars = br.readLine().toCharArray();
            int[] idx = new int[26];
            Arrays.fill(idx, -1);
            for (int i=0; i<chars.length; i++) {
            	int j = idx[chars[i]-'a'];
                if (j != -1 && i-j != 1) {
                    cnt--;
                    break;
                }
                idx[chars[i]-'a'] = i;
            }            
        }

        System.out.println(cnt);
    }
}