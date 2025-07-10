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
        
        int max = -1;
        int r = -1;
        int c = -1;
        
        for (int i=1; i<=9; i++) {
        	st = new StringTokenizer(br.readLine());
        	for (int j=1; j<=9; j++) {
        		int num = Integer.parseInt(st.nextToken());
        		if (num > max) {
        			max = num;
        			r = i;
        			c = j;
        		}
    		}
        }
        sb.append(max);
        sb.append("\n").append(r).append(" ").append(c);
        System.out.println(sb.toString());
        
        
    }
}