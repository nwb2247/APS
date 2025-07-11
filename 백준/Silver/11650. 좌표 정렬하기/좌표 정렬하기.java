import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        
        int N = Integer.parseInt(br.readLine());
        int[][] arr = new int[N][2];
        for (int i=0; i<N; i++) {
        	st = new StringTokenizer(br.readLine());
        	arr[i][0] = Integer.parseInt(st.nextToken());
        	arr[i][1] = Integer.parseInt(st.nextToken());
        }
        
        Arrays.sort(arr, (o1, o2) -> {
        	
        	if (o1[0] > o2[0]) {
        		return 1;
        	} else if (o1[0] < o2[0]){
        		return -1;
        	} else {
        		if (o1[1] > o2[1]) {
        			return 1;
        		} else {
        			return -1;
        		}
        	}
        });
        
        for (int[] a : arr) {
        	sb.append(a[0]).append(" ").append(a[1]).append("\n");
        }
        System.out.println(sb.toString());    
        
    }
}