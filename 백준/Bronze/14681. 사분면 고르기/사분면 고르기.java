import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int X = Integer.parseInt(br.readLine());
		int Y = Integer.parseInt(br.readLine());
		
		int sol = 1;
		
		if (X*Y < 0 ) {
			sol++;
		}
		
		if (Y < 0) {
			sol+=2;
		}
		
		System.out.println(sol);
		
		
		
	}
	
}