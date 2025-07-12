import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	
    	int[] arr = new int[8];
    	for (int i=0; i<8; i++) {
    		arr[i] = Integer.parseInt(st.nextToken());
    	}
    	boolean a = true;
    	boolean d = true;
    	for (int i=1; i<8; i++) {
    		if (arr[i] > arr[i-1]) {
    			d = false;
    		} else {
    			a = false;
    		}
    	}
    	if (!a && !d) {
    		System.out.println("mixed");
    	} else if (a) {
    		System.out.println("ascending");
    	} else {
    		System.out.println("descending");
    	}
    	
    }
      
}