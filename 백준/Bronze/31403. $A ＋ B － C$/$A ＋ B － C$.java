import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringBuilder sb = new StringBuilder();
    	
    	String a = br.readLine();
    	String b = br.readLine();
    	int c = Integer.parseInt(br.readLine());
    	
    	sb.append(Integer.parseInt(a)+Integer.parseInt(b)-c);
    	sb.append("\n");
    	sb.append(Integer.parseInt(a+b)-c);
    	
    	System.out.println(sb.toString());
    	
    }
      
}