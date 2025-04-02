import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int money = 1000 - Integer.parseInt(br.readLine());
		
		int[] coinType = {500, 100 , 50, 10 , 5, 1};
		
		int count = 0;
		for (int c : coinType) {
			count += money / c;
			money = money % c;
			if (money == 0) {
				break;
			}
		}
		
		System.out.println(count);

	}

}
