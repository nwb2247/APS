import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws Exception {
	
		Scanner sc = new Scanner(System.in);
		
		int a = (int) 'a'; // 97
		int z = (int) 'z'; // 122
		int A = (int) 'A'; // 65
		int Z = (int) 'Z'; // 90
		int zero = (int) '0'; // 48
		int nine = (int) '9'; // 57
		
		StringBuilder sb = new StringBuilder();
		
		while (sc.hasNextLine()) { // 테스트 케이스 갯수가 정해져 있지 않은 경우에는 br대신 Scanner를 사용하자 	
			
			char[] chars = sc.nextLine().toCharArray();
			int upper = 0;
			int lower = 0;
			int number = 0;
			for (char c : chars) {
				if ((int) c >=A && (int) c <=Z) upper++;
				if ((int) c >=a && (int) c <=z) lower++;
				if ((int) c >=zero && (int) c <=nine) number++;
			}
			
			int blank = chars.length - (upper + lower + number);
			
			sb.append(lower + " " + upper + " " + number + " " + blank + "\n");
		}
		
	System.out.println(sb);

	}

}
