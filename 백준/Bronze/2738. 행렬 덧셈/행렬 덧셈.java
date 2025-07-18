import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] mat = new int[N][M];
        for (int i=0; i<N; i++) {
        	st = new StringTokenizer(br.readLine());
        	for (int j=0; j<M; j++) {
        		mat[i][j] = Integer.parseInt(st.nextToken());
        	}
        }
        for (int i=0; i<N; i++) {
        	st = new StringTokenizer(br.readLine());
        	for (int j=0; j<M; j++) {
        		mat[i][j] += Integer.parseInt(st.nextToken());
        	}
        }
        for (int i=0; i<N; i++) {
        	for (int j=0; j<M; j++) {
        		sb.append(mat[i][j]).append(" ");
        	}
        	sb.append("\n");
        }
        System.out.println(sb.toString());
        
        
    }
}