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
    	int len = 0;
    	int cur = num;
    	while (cur > 0) {
    		if (cur%10 == 6) {
    			len++;
    			if (len == 3) {
    				return true;
    			}
    		} else {
    			len = 0;
    		}
    		cur/=10;
    	}
    	return false;
    }
    
}