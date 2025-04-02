import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		outer : 
		for (int i=0; i<N; i++) {
			
			int[] Acnt = new int[5];
			int[] Bcnt = new int[5];
			
			st = new StringTokenizer(br.readLine());
			int Anum = Integer.parseInt(st.nextToken());
			for (int j=0; j<Anum; j++) {
				int type = Integer.parseInt(st.nextToken());
				Acnt[type]++;
			}
			st = new StringTokenizer(br.readLine());
			int Bnum = Integer.parseInt(st.nextToken());
			for (int j=0; j<Bnum; j++) {
				int type = Integer.parseInt(st.nextToken());
				Bcnt[type]++;
			}
			
			int type = 4;
			while (type > 0) {
				if (Acnt[type] != Bcnt[type]) {
					if (Acnt[type] > Bcnt[type]) {
						System.out.println("A");
					} else {
						System.out.println("B");
					}
					continue outer;
				}
				type--;
			}
			
			System.out.println("D");
			
			
			
		}
		 

	}

}
