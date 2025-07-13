import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static class info implements Comparable<info> {
		int age;
		String name;
		int id;
		
		public info(int age, String name, int id) {
			this.age = age;
			this.name = name;
			this.id = id;
		}

		@Override
		public int compareTo(Main.info o) {
			if (age > o.age) {
				return 1;
			} else if (age == o.age && id > o.id) {
				return 1;
			} else {
				return -1;
			}
		}
		
		
	}

    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringBuilder sb = new StringBuilder();
    	StringTokenizer st;
    	
    	int N = Integer.parseInt(br.readLine());
    	info[] arr = new info[N];
    	int id = 0;
    	for (int i=0; i<N; i++) {
    		st = new StringTokenizer(br.readLine());
    		arr[i] = new info(Integer.parseInt(st.nextToken()), st.nextToken(), ++id);
    	}
    	Arrays.sort(arr);
    	for (info i : arr) {
    		sb.append(i.age).append(" ").append(i.name).append("\n");
    	}
    	System.out.println(sb.toString());
    	
    }
    
}