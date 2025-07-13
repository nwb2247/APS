import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringBuilder sb = new StringBuilder();
    	StringTokenizer st;
    	
    	ArrayList<ArrayList<Integer>> map = new ArrayList<>();
    	for (int i=0; i<=200001; i++) {
    		map.add(new ArrayList<>());
    	}
    	
    	int N = Integer.parseInt(br.readLine());
    	
    	for (int i=0; i<N; i++) {
    		st = new StringTokenizer(br.readLine());
    		int x = Integer.parseInt(st.nextToken());
    		int y = Integer.parseInt(st.nextToken());
    		map.get(y+100000).add(x);
    	}
    	for (int i=0; i<200001; i++) {
    		map.get(i).sort(Comparator.naturalOrder());
    		for (int j=0; j<map.get(i).size(); j++) {
    			sb.append(map.get(i).get(j)).append(" ").append(i-100000);
    			sb.append("\n");
    		}
    	}
    	System.out.println(sb.toString());
    	
    }
    
}