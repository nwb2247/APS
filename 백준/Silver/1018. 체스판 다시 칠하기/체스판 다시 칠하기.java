import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        char[][] ver1 = new char[8][8];
        for (int i=0; i<8; i++) {
        	if (i%2 == 0) {
        		ver1[i] = new char[] {'B','W','B','W','B','W','B','W'};
        	} else {
        		ver1[i] = new char[] {'W','B','W','B','W','B','W','B'};
        	}
        }
        char[][] ver2 = new char[8][8];
        for (int i=0; i<8; i++) {
        	if (i%2 != 0) {
        		ver2[i] = new char[] {'B','W','B','W','B','W','B','W'};
        	} else {
        		ver2[i] = new char[] {'W','B','W','B','W','B','W','B'};
        	}
        }
        
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        char[][] map = new char[N][M];
        for (int i=0; i<N; i++) {
        	String input = br.readLine();
        	for (int j=0; j<M; j++) {
        		map[i][j] = input.charAt(j);
        	}
        }
        
        int min = Integer.MAX_VALUE;
        for (int i=0; i<=N-8; i++) {
        	for (int j=0; j<=M-8; j++) {
        		int cnt1 = 0;
        		int cnt2 = 0;
        		for (int r=0; r<8; r++) {
        			for (int c=0; c<8; c++) {
        				if (map[i+r][j+c] != ver1[r][c]) cnt1++;
        				if (map[i+r][j+c] != ver2[r][c]) cnt2++;
        			}
        		}
        		min = Math.min(min, Math.min(cnt1, cnt2));
        	}
        }
        
        System.out.println(min);
        
    }
}