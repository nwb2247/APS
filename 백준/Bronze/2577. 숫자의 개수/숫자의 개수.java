import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringBuilder sb = new StringBuilder();
    	
    	int mul = 1;
    	for (int i=0; i<3; i++) {
    		mul *= Integer.parseInt(br.readLine());
    	}
    	char[] chars = String.valueOf(mul).toCharArray();
    	int[] cnt = new int[10];
    	for (char c : chars) {
    		cnt[c-'0']++;
    	}
    	for (int c : cnt) {
    		sb.append(c).append("\n");
    	}
    	System.out.println(sb.toString());
    	
    }
      
}