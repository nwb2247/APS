import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int N = Integer.parseInt(br.readLine());
    	
    	int cur = 666;
    	for (int i=0; i<N; i++) {
    		while (!check(cur)) {
    			cur++;
    		}
    		cur++;
    		
    	}
    	cur--;
    	System.out.println(cur);
    	
    }
    
    public static boolean check(int num) {
    	char[] chars = String.valueOf(num).toCharArray();
    	int len = 0;
    	for (char c : chars) {
    		if (c == '6') {
    			len++;
    			if (len == 3) {
    				return true;
    			}
    		} else {
    			len = 0;
    		}
    	}
    	return false;
    }
    
}