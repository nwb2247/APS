import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	
	//BJ2193 이친수
	
	public static void main(String[] args) throws Exception {
		
		long zeroEnd = 0;
		long oneEnd = 1;
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		for (int i=2; i<=N; i++) {
			long newOneEnd = zeroEnd;
			long newZeroEnd = oneEnd + zeroEnd;
			
			zeroEnd = newZeroEnd;
			oneEnd = newOneEnd;
		}
		
		System.out.println(zeroEnd + oneEnd);
				
	}

}
