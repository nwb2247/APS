import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	char[] chars = br.readLine().toCharArray();
    	int idx = -1;
    	int sum = 0;
    	for (int i=0; i<13; i++) {
    		if (chars[i] == '*') {
    			idx = i; 
    		} else if (i!=12){
    			if (i%2==0) {
    				sum += chars[i]-'0';
    			} else {
        			sum += 3*(chars[i]-'0');
        		}
    		} 
    	}
    	if (idx == 12) {
    		int num = 10-(sum%10);
    		if (num == 10) {
    			System.out.println(0);
    		} else {
    			System.out.println(num);
    		}
    		return;
    	}
    	
    	int c = idx%2==0?1:3;
    	for (int i=0; i<=9; i++) {
    		int num = 10 - (sum+c*i)%10;
    		if ((num == 10 && chars[12]-'0' == 0)
    				|| num == chars[12]-'0') {
    			System.out.println(i);
    			break;
    		}
    	}
    	
    	
    }
      
}