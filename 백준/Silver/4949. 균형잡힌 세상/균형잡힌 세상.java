import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
	
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        String s = br.readLine();
        ArrayDeque<Character> stack = new ArrayDeque<>();
        while (!s.equals(".")) {
        	stack.clear();
        	boolean wrong = false;
        	char[] chars = s.toCharArray();
        	for (char c : chars) {
        		if (c == '[' || c == '(') {
        			stack.offerLast(c);
        		} else if (c == ']') {
        			
        			if (stack.isEmpty() || stack.peekLast() != '[') {
        				wrong = true;
        				break;
        			} else {
        				stack.pollLast();
        			}
        		} else if (c == ')') {
        			if (stack.isEmpty() || stack.peekLast() != '(') {
        				wrong = true;
        				break;
        			} else {
        				stack.pollLast();
        			}
        		}
        	}
        	if (!stack.isEmpty()) wrong = true;
        	if (wrong) {
        		sb.append("no");
        	} else {
        		sb.append("yes");
        	}
        	sb.append("\n");
        	s = br.readLine();
        }
        System.out.println(sb.toString());
    }
}