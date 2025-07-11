import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	
	public static boolean recur(int[] digit, int sum, int s, int N) {
		
		if (s==-1) {
			if (sum == N) {
				return true;
			} else {
				return false;
			}
		}
		
		int co = (int) Math.pow(10, s) + 1;
		for (int i=0; i<10; i++) {
			int newSum = sum + i*co;
			if (newSum > N) break;
			digit[s] = i;
			if (recur(digit, newSum, s-1, N)) {
				return true;
			}
		}
		
		return false;
		
	}
	
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        int N = Integer.parseInt(br.readLine());
        
        int s = 0;
        int N1 = N;
        while (N1 >= 10) {
        	N1 /= 10;
        	s++;
        }
        
        int[] digit = new int[s+1];
        
        if (recur(digit, 0, s, N)) {
        	for (int i=s; i>=0; i--) {
            	sb.append(digit[i]);
            }
            System.out.println(Integer.parseInt(sb.toString()));
        } else {
        	System.out.println(0);
        }

        
        
    }
}