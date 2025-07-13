import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
	
	static class Info {
		
		int id, prio;

		public Info(int id, int prio) {
			this.id = id;
			this.prio = prio;
		}

		@Override
		public String toString() {
			return "Info [id=" + id + ", prio=" + prio + "]";
		}		
		
	}

    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st;
    	StringBuilder sb = new StringBuilder();
    			
    	int T = Integer.parseInt(br.readLine());
    	
    	for (int t=0; t<T; t++) {
    		
        	ArrayList<HashSet<Integer>> setList = new ArrayList<>();
        	for (int i=0; i<=9; i++) {
        		setList.add(new HashSet<>());
        	}
        	
        	ArrayDeque<Info> q = new ArrayDeque<>();
        	
        	st = new StringTokenizer(br.readLine());
        	int N = Integer.parseInt(st.nextToken());
        	int M = Integer.parseInt(st.nextToken());
        	
        	st = new StringTokenizer(br.readLine());
        	int id = 0;
        	for (int i=0; i<N; i++) {
        		int p = Integer.parseInt(st.nextToken());
        		q.addLast(new Info(id, p));
        		setList.get(p).add(id++);
        	}
    		
        	int order = 1;
        	outer : 
    		while (true) {
    			Info cur = q.pollFirst();
    			for (int p=cur.prio+1; p<=9; p++) {
    				if (!setList.get(p).isEmpty()) {
    					q.addLast(cur);
    					continue outer;
    				}
    			}
    			if (cur.id == M) {
    				break;
    			}
    			setList.get(cur.prio).remove(cur.id);
    			order++;
    		}
        	
        	sb.append(order).append("\n");
	
    	}
    	
    	System.out.println(sb.toString());
    }
    	
    	
    	
    	
    
}