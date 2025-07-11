import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        char[][] map = new char[5][];
        int maxlen = 0;
        for (int i=0; i<5; i++) {
        	map[i] = br.readLine().toCharArray();
        	maxlen = Math.max(maxlen, map[i].length);
        }
        
        for (int i=0; i<maxlen; i++) {
        	for (int j=0; j<5; j++) {
        		if (i < map[j].length) sb.append(map[j][i]);
        	}
        }
        
        System.out.println(sb.toString());
        
    }
}