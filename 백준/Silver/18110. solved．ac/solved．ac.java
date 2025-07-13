import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	int N = Integer.parseInt(br.readLine());
    	int[] cnt = new int[31];
    	for (int i=0; i<N; i++) {
    		cnt[Integer.parseInt(br.readLine())]++;
    	}
    	
    	int cutNum = (int) Math.round(N * 0.15);
    	int cut = cutNum;
    	int i=1;
    	while (cut != 0) {
    		if (cnt[i] <= cut) {
    			cut -= cnt[i];
    			cnt[i] = 0;
    		} else {
    			cnt[i] -= cut;
    			cut = 0;
    		}
    		i++;
    	}
    	i=30;
    	cut = cutNum;
    	while (cut != 0) {
    		if (cnt[i] <= cut) {
    			cut -= cnt[i];
    			cnt[i] = 0;
    		} else {
    			cnt[i] -= cut;
    			cut = 0;
    		}
    		i--;
    	}
    	int sum = 0;
    	for (int j=1; j<=30; j++) {
    		sum += cnt[j]*j;
    	}
    	System.out.println(Math.round((double) sum / (N-2*cutNum)));
    	
    }
    
}