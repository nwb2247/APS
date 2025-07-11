import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
	
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        
        int N = Integer.parseInt(br.readLine());
        int[][] arr = new int[N][2];
        for (int i=0; i<N; i++) {
        	st = new StringTokenizer(br.readLine());
        	arr[i][0] = Integer.parseInt(st.nextToken());
        	arr[i][1] = Integer.parseInt(st.nextToken());
        }
        
        int[] cnt = new int[N];
        
        for (int i=0; i<N; i++) {
        	cnt[i]++;
        	for (int j=0; j<N; j++) {
        		if (arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1]) {
        			cnt[i]++;
        		}
        	}
        }
        
        for (int i=0; i<N; i++) {
        	sb.append(cnt[i]).append(" ");
        }
        
        System.out.println(sb.toString());
    }
}