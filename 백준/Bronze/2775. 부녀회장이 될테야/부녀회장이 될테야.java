import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        int[][] map = new int[15][15];
        for (int i=1; i<15; i++) {
        	map[0][i] = i;
        }
        for (int i=1; i<15; i++) {
        	for (int j=1; j<15; j++) {
        		map[i][j] = map[i][j-1]+map[i-1][j];
        	}
        }        
        
        int T = Integer.parseInt(br.readLine());
        for (int t=0; t<T; t++) {
        	int k = Integer.parseInt(br.readLine());
        	int n = Integer.parseInt(br.readLine());
        	sb.append(map[k][n]).append("\n");
        }
        System.out.println(sb.toString());
        
    }
}