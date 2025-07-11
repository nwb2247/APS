import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        boolean[][] map = new boolean[100][100];
        int N = Integer.parseInt(br.readLine());
        for (int n=0; n<N; n++) {
        	st = new StringTokenizer(br.readLine());
        	int c = Integer.parseInt(st.nextToken());
        	int r = Integer.parseInt(st.nextToken());
        	for (int i=r; i<r+10; i++) {
        		for (int j=c; j<c+10; j++) {
        			map[i][j] = true;
        		}
        	}
        }
        
        int cnt = 0;
        for (int i=0; i<100; i++) {
    		for (int j=0; j<100; j++) {
    			if (map[i][j]) cnt++;
    		}
    	}
        
        System.out.println(cnt);
        
    }
}