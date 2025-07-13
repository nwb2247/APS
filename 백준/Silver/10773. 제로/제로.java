import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class Main {

    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringBuilder sb = new StringBuilder();
    	
    	int N = Integer.parseInt(br.readLine());
    	ArrayDeque<Integer> stack = new ArrayDeque<>();
    	for (int i=0; i<N; i++) {
    		int cur = Integer.parseInt(br.readLine());
    		if (cur == 0) {
    			stack.pollLast();
    		} else {
    			stack.offerLast(cur);
    		}
    	}
    	int sum = 0;
    	while(!stack.isEmpty()) {
    		sum += stack.pollLast();
    	}
    	System.out.println(sum);
    	
    }
    
}