import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringBuilder sb = new StringBuilder();
    	int N= Integer.parseInt(br.readLine());
    	boolean[] arr = new boolean[2000001];
    	for (int i=0; i<N; i++) {
    		arr[1000000 + Integer.parseInt(br.readLine())] = true;
    	}
    	for (int i=0; i<=2000000; i++) {
    		if (arr[i]) sb.append(i-1000000).append("\n");
    	}
    	System.out.println(sb.toString());
    	
    }
    
}